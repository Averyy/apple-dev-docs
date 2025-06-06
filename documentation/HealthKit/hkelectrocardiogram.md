# HKElectrocardiogram

**Framework**: HealthKit  
**Kind**: class

A sample for electrocardiogram data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class HKElectrocardiogram
```

#### Overview

An [`HKElectrocardiogram`](hkelectrocardiogram.md) is a collection of voltage values representing waveforms from one or more leads. The [`HKElectrocardiogram`](hkelectrocardiogram.md) sample provides high-level details about the ECG reading, such as the sampling frequency or classification. HealthKit provides read-only access to electrocardiogram (ECG) data saved by Apple Watch.

You can query for [`HKElectrocardiogram`](hkelectrocardiogram.md) samples using an [`HKSampleQuery`](hksamplequery.md).

```swift
// Create the electrocardiogram sample type.
let ecgType = HKObjectType.electrocardiogramType()


// Query for electrocardiogram samples
let ecgQuery = HKSampleQuery(sampleType: ecgType,
                             predicate: nil,
                             limit: HKObjectQueryNoLimit,
                             sortDescriptors: nil) { (query, samples, error) in
    if let error = error {
        // Handle the error here.
        fatalError("*** An error occurred \(error.localizedDescription) ***")
    }
    
    guard let ecgSamples = samples as? [HKElectrocardiogram] else {
        fatalError("*** Unable to convert \(String(describing: samples)) to [HKElectrocardiogram] ***")
    }
    
    for sample in ecgSamples {
        // Handle the samples here.
        
    }
}

// Execute the query.
healthStore.execute(ecgQuery)
```

After retrieving an [`HKElectrocardiogram`](hkelectrocardiogram.md) sample, you can access the voltage measurements associated with the sample use an [`HKElectrocardiogramQuery`](hkelectrocardiogramquery.md) query.

```swift
// Create a query for the voltage measurements
let voltageQuery = HKElectrocardiogramQuery(ecgSample) { (query, result) in
    switch(result) {
    
    case .measurement(let measurement):
        if let voltageQuantity = measurement.quantity(for: .appleWatchSimilarToLeadI) {
            // Do something with the voltage quantity here.

        }
    
    case .done:
        // No more voltage measurements. Finish processing the existing measurements.

    case .error(let error):
        // Handle the error here.

    }
}

// Execute the query.
healthStore.execute(voltageQuery)
```

## Topics

### Accessing Overview Information
- [var classification: HKElectrocardiogram.Classification](hkelectrocardiogram/classification-swift.property.md)
  The ECG’s classification.
- [HKElectrocardiogram.Classification](hkelectrocardiogram/classification-swift.enum.md)
  Classifications returned by Apple Watch’s ECG algorithm.
- [var averageHeartRate: HKQuantity?](hkelectrocardiogram/averageheartrate.md)
  The user’s average heart rate during the ECG.
- [var symptomsStatus: HKElectrocardiogram.SymptomsStatus](hkelectrocardiogram/symptomsstatus-swift.property.md)
  A value that indicates whether the user entered a symptom when they recorded the ECG.
- [HKElectrocardiogram.SymptomsStatus](hkelectrocardiogram/symptomsstatus-swift.enum.md)
  Values indicating whether the user entered a symptom when they recorded the ECG.
### Accessing Voltage Measurements
- [var numberOfVoltageMeasurements: Int](hkelectrocardiogram/numberofvoltagemeasurements.md)
  The number of voltage measurements associated with this sample.
- [var samplingFrequency: HKQuantity?](hkelectrocardiogram/samplingfrequency.md)
  The frequency at which the Apple Watch sampled the voltage.
- [HKElectrocardiogram.VoltageMeasurement](hkelectrocardiogram/voltagemeasurement.md)
  The voltage for all leads at a single point in time.
- [HKElectrocardiogram.Lead](hkelectrocardiogram/lead.md)
  The lead used to record a voltage measurement.
### Specifying Metadata
- [let HKMetadataKeyAppleECGAlgorithmVersion: String](hkmetadatakeyappleecgalgorithmversion.md)
  A key for metadata indicating the version number of the algorithm Apple Watch uses to generate an ECG reading.
- [enum HKAppleECGAlgorithmVersion](hkappleecgalgorithmversion.md)
  Version numbers for the algorithm Apple Watch uses to generate an ECG reading.
### Specifying Predicate Key Paths
- [let HKPredicateKeyPathECGClassification: String](hkpredicatekeypathecgclassification.md)
  The key path for the sample’s classification.
- [let HKPredicateKeyPathECGSymptomsStatus: String](hkpredicatekeypathecgsymptomsstatus.md)
  The key path for the sample’s symptom status.
- [let HKPredicateKeyPathAverageHeartRate: String](hkpredicatekeypathaverageheartrate.md)
  The key path for the sample’s average heart rate.

## Relationships

### Inherits From
- [HKSample](hksample.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [HKElectrocardiogram.VoltageMeasurement](hkelectrocardiogram/voltagemeasurement.md)
  The voltage for all leads at a single point in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogram)*