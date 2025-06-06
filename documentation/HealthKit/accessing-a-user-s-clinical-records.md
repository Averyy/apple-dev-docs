# Accessing a User’s Clinical Records

**Framework**: HealthKit

Request authorization to query HealthKit for a user’s clinical records and display them in your app.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Xcode 13.2+

#### Overview

This sample demonstrates how to request access to a user’s clinical records through [`HealthKit`](HealthKit.md). With the HealthKit framework’s clinical record support, you can read [`Fast Healthcare Interoperability Resources`](https://developer.apple.comhttp://hl7.org/fhir) (FHIR) objects from the HealthKit store. People must first download their clinical records from one of the [`supported healthcare institutions`](https://developer.apple.comhttps://support.apple.com/en-us/HT208647) before the records appear in HealthKit.

##### Configure the Sample Code Project

To use HealthKit, you must first enable the HealthKit capability and include the [`NSHealthShareUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSHealthShareUsageDescription) key in your app’s `Info.plist` file, as described in [`Accessing Health Records`](accessing-health-records.md). To access the clinical records, check the Clinical Health Records checkbox in the HealthKit capability and include the [`NSHealthClinicalHealthRecordsShareUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSHealthClinicalHealthRecordsShareUsageDescription) key in your app’s `Info.plist` file.

The sample app enables the capability and provides the usage string.

Before building and running the app:

1. Set a valid signing team in the target’s General pane so that Xcode can create a provisioning profile containing the HealthKit entitlement when you build the app for the first time.
2. Add sample data to the Health app by connecting a valid patient portal account from a [`supported healthcare institutions`](https://developer.apple.comhttps://support.apple.com/en-us/HT208647). If you don’t have such an account, you can add sample data within the Simulator as described in [`Accessing Sample Data in the Simulator`](accessing-sample-data-in-the-simulator.md).

When you first run the app, it hasn’t requested permission to read or share any data in HealthKit. Tapping any items in the list results in an Authorization not Determined error. To authorize the app, scroll to the bottom of the list, and tap the Authorize button.

##### Define the Sample Types to Request

The app defines the clinical record sample types using the [`HKClinicalTypeIdentifier`](HKClinicalTypeIdentifier.md) enumeration. The app must request permission to read all the types that it intends to use. Note that the app may define both clinical records and standard HealthKit sample types at the same time.

```swift
/// An enumeration that defines two categories of data types: Health Records and Fitness Data.
/// Health Records enumerates the clinical records the app would like to access and Fitness Data contains the
/// fitness data types.
enum Section {
    case healthRecords
    case fitnessData
    
    var displayName: String {
        switch self {
        case .healthRecords:
            return "Health Records"
        case .fitnessData:
            return "Fitness Data"
        }
    }
    
    var types: [HKSampleType] {
        switch self {
        case .healthRecords:
            return [
                HKObjectType.clinicalType(forIdentifier: .allergyRecord)!,
                HKObjectType.clinicalType(forIdentifier: .vitalSignRecord)!,
                HKObjectType.clinicalType(forIdentifier: .conditionRecord)!,
                HKObjectType.clinicalType(forIdentifier: .immunizationRecord)!,
                HKObjectType.clinicalType(forIdentifier: .labResultRecord)!,
                HKObjectType.clinicalType(forIdentifier: .medicationRecord)!,
                HKObjectType.clinicalType(forIdentifier: .procedureRecord)!
            ]
        
        case .fitnessData:
            return [
                HKObjectType.quantityType(forIdentifier: .stepCount)!,
                HKObjectType.quantityType(forIdentifier: .distanceWalkingRunning)!
            ]
        }
    }
}
```

##### Request Authorization

The app may request authorization to access both clinical data and HealthKit data simultaneously.

```swift
/// Create an instance of the health store. Use the health store to request authorization to access
/// HealthKit records and to query for the records.
let healthStore = HKHealthStore()

var sampleTypes: Set<HKSampleType> {
    return Set(Section.healthRecords.types + Section.fitnessData.types)
}

/// Before accessing clinical records and other health data from HealthKit, the app must ask the user for
/// authorization. The health store's getRequestStatusForAuthorization method allows the app to check
/// if user has already granted authorization. If the user hasn't granted authorization, the app
/// requests authorization from the person using the app.
@objc
func requestAuthorizationIfNeeded(_ sender: AnyObject? = nil) {
    healthStore.getRequestStatusForAuthorization(toShare: Set(), read: sampleTypes) { (status, error) in
        if status == .shouldRequest {
            self.requestAuthorization(sender)
        } else {
            DispatchQueue.main.async {
                let message = "Authorization status has been determined, no need to request authorization at this time"
                self.present(message: message, titled: "Already Requested")
            }
        }
    }
}

/// The health store's requestAuthorization method presents a permissions sheet to the user, allowing the user to
/// choose what data they allow the app to access.
@objc
func requestAuthorization(_ sender: AnyObject? = nil) {
    healthStore.requestAuthorization(toShare: nil, read: sampleTypes) { (success, error) in
        guard success else {
            DispatchQueue.main.async {
                self.handleError(error)
            }
            return
        }
    }
}
```

Typically, apps that read or share HealthKit data automatically request authorization–either when the app first launches or just before the app needs to access the data. However, to provide readers with complete control over the authorization process, this sample code doesn’t automatically request authorization. Instead, anyone using the app must manually request authorization, by scrolling to the bottom of the list and tapping the Authorize button.

##### Query for Health Records

To query for clinical records, the app uses an [`HKSampleQuery`](HKSampleQuery.md) as shown below.

```swift
/// Use HKSampleQuery to query the HealthKit store for samples by type.
func queryForSamples() {
    let sortDescriptors = [NSSortDescriptor(key: HKSampleSortIdentifierStartDate, ascending: false)]
    let query = HKSampleQuery(sampleType: sampleType, predicate: nil, limit: 100, sortDescriptors: sortDescriptors) {(_, samplesOrNil, error) in
        DispatchQueue.main.async {
            guard let samples = samplesOrNil else {
                self.handleError(error)
                return
            }
            
            self.samples = samples
            self.tableView.reloadData()
        }
    }
    
    healthStore.execute(query)
}
```

##### Access Elements Within a Fhir Resource

After a person using the app has given the app access to their clinical records, the app needs to extract the relevant information from the FHIR JSON data so that it can do something useful with it. For example, to display the status of a medication in the form of a [`MedicationStatement`](https://developer.apple.comhttp://hl7.org/fhir/DSTU2/medicationstatement) resource, the app needs to access the `MedicationStatement.status` element.

The app uses the [`FHIRModels`](https://developer.apple.comhttps://github.com/apple/FHIRModels) library to parse the JSON data into Swift classes. For more details on FHIRModels, see [`Handling FHIR Without Getting Burned`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2020/10669).

It uses a `JSONDecoder` to convert the resource’s JSON data:

```swift
/// Each clincal record retrieved from HealthKit is associated with a FHIR Resource. Decode it using the FHIRModels.
func decode(resource: HKFHIRResource) throws -> DisplayItemSubtitleConvertible {
    if #available(iOS 14.0, *) {
        switch resource.fhirVersion.fhirRelease {
        case .dstu2:
            return try decodeDSTU2(resource: resource)
        case .r4:
            return try decodeR4(resource: resource)
        default:
            throw FHIRResourceDecodingError.versionNotSupported(resource.fhirVersion.stringRepresentation)
        }
    } else {
        return try decodeDSTU2(resource: resource) // On iOS 12 and 13, HealthKit always uses DSTU2 encoding for FHIR resources.
    }
}
```

This provides direct access to the `status` element, so that the app can display it. It appears as the subtitle of the Medication list view.

```swift
extension ModelsDSTU2.MedicationStatement: DisplayItemSubtitleConvertible {
    var displayItemSubtitle: String {
        return self.status.value?.rawValue ?? "unknown"
    }
}
```

## See Also

- [Accessing Health Records](accessing-health-records.md)
  Read clinical record data from the HealthKit store.
- [Accessing Sample Data in the Simulator](accessing-sample-data-in-the-simulator.md)
  Set up sample accounts to build and test your app.
- [Accessing Data from a SMART Health Card](accessing-data-from-a-smart-health-card.md)
  Query for and validate a verifiable clinical record.
- [class HKClinicalRecord](hkclinicalrecord.md)
  A sample that stores a clinical record.
- [class HKFHIRResource](hkfhirresource.md)
  An object containing Fast Healthcare Interoperability Resources (FHIR) data.
- [class HKVerifiableClinicalRecord](hkverifiableclinicalrecord.md)
  A sample that represents the contents of a SMART Health Card or EU Digital COVID Certificate.
- [class HKVerifiableClinicalRecordSubject](hkverifiableclinicalrecordsubject.md)
  The subject associated with a signed clinical record.
- [class HKCDADocumentSample](hkcdadocumentsample.md)
  A Clinical Document Architecture (CDA) sample that stores a single document.
- [class HKDocumentSample](hkdocumentsample.md)
  An abstract class that represents a health document in the HealthKit store.
- [static let CDA: HKDocumentTypeIdentifier](hkdocumenttypeidentifier/cda.md)
  The CDA Document type identifier, used when requesting permission to read or share CDA documents.
- [class HKDocumentType](hkdocumenttype.md)
  A sample type used to create queries for documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/accessing-a-user-s-clinical-records)*