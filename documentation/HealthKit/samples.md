# Samples

**Framework**: HealthKit

Create and save health and fitness samples.

#### Overview

The HealthKit store saves most health and fitness data using [`HKSample`](hksample.md) subclasses. All sample subclasses record information at a specified time. If the sample’s [`startDate`](hksample/startdate.md) and [`endDate`](hksample/enddate.md) properties are the same, the sample represents a point in time. If the [`endDate`](hksample/enddate.md) is after the [`startDate`](hksample/startdate.md), the sample represents a time interval.

HealthKit uses different [`HKSample`](hksample.md) subclasses to store different types of data:

- [`HKQuantitySample`](hkquantitysample.md) objects store quantities—a numerical value and units. Most HealthKit data types use quantity samples. For example, height, heart rate, and dietary energy consumed all use quantity samples.
- [`HKCategorySample`](hkcategorysample.md) objects store a single option selected from a short list. For example, category samples record sleep data (the user can be in bed, asleep, or awake).
- [`HKCorrelation`](hkcorrelation.md) samples combine two or more samples into a single value. For example, correlation samples represent food intake and blood pressure samples. A food sample contains any number of nutrition samples, while a blood pressure sample contains both a systolic and a diastolic sample.
- HealthKit represents specialized data types with sample subclasses such as [`HKCDADocumentSample`](hkcdadocumentsample.md), [`HKWorkoutRoute`](hkworkoutroute.md), and [`HKWorkout`](hkworkout.md).

## Topics

### Essentials
- [Saving data to HealthKit](saving-data-to-healthkit.md)
  Create and share HealthKit samples.
- [Reading and Writing HealthKit Series Data](reading-and-writing-healthkit-series-data.md)
  Share and read heartbeat and quantity series data using series builders and queries.
### Basic samples
- [class HKCumulativeQuantitySample](hkcumulativequantitysample.md)
  A sample that represents a cumulative quantity.
- [class HKDiscreteQuantitySample](hkdiscretequantitysample.md)
  A sample that represents a discrete quantity.
- [class HKQuantitySample](hkquantitysample.md)
  A sample that represents a quantity, including the value and the units.
- [class HKCategorySample](hkcategorysample.md)
  A sample with values from a short list of possible values.
- [class HKCorrelation](hkcorrelation.md)
  A sample that groups multiple related samples into a single entry.
- [Units and quantities](units-and-quantities.md)
  Objects used to specify a quantity for a given unit, and to convert between units.
- [Metadata Keys](metadata-keys.md)
  Constants used to add metadata to objects stored in HealthKit.
### Series data
- [class HKQuantitySeriesSampleBuilder](hkquantityseriessamplebuilder.md)
  A builder object for incrementally building a sample that contains multiple quantities.
- [class HKHeartbeatSeriesBuilder](hkheartbeatseriesbuilder.md)
  A builder object for incrementally building a heartbeat series.
- [class HKHeartbeatSeriesSample](hkheartbeatseriessample.md)
  A sample that represents a series of heartbeats.
### Electrocardiograms
- [class HKElectrocardiogram](hkelectrocardiogram.md)
  A sample for electrocardiogram data.
- [HKElectrocardiogram.VoltageMeasurement](hkelectrocardiogram/voltagemeasurement.md)
  The voltage for all leads at a single point in time.
### Audiograms
- [class HKAudiogramSample](hkaudiogramsample.md)
  A sample that stores an audiogram.
- [class HKAudiogramSensitivityPoint](hkaudiogramsensitivitypoint.md)
  A hearing sensitivity reading associated with a hearing test.
### Medical records
- [Accessing Health Records](accessing-health-records.md)
  Read clinical record data from the HealthKit store.
- [Accessing Sample Data in the Simulator](accessing-sample-data-in-the-simulator.md)
  Set up sample accounts to build and test your app.
- [Accessing a User’s Clinical Records](accessing-a-user-s-clinical-records.md)
  Request authorization to query HealthKit for a user’s clinical records and display them in your app.
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
### Vision prescriptions
- [class HKVisionPrescription](hkvisionprescription.md)
  A sample that stores a vision prescription.
- [class HKGlassesPrescription](hkglassesprescription.md)
  A sample that stores a prescription for glasses.
- [class HKContactsPrescription](hkcontactsprescription.md)
  A sample that store a prescription for contacts.
- [class HKGlassesLensSpecification](hkglasseslensspecification.md)
  An object that contains the glasses prescription data for one eye.
- [class HKContactsLensSpecification](hkcontactslensspecification.md)
  An object that contains the contacts prescription data for one eye.
- [class HKLensSpecification](hklensspecification.md)
  An abstract superclass for lens specifications.
- [class HKVisionPrism](hkvisionprism.md)
  Prescription data for eye alignment.
- [class HKPrescriptionType](hkprescriptiontype.md)
  A type that identifies samples that store a prescription.
### Walking steadiness classifications
- [enum HKAppleWalkingSteadinessClassification](hkapplewalkingsteadinessclassification.md)
  A classification of a score based on the steadiness of the user’s gait.
- [HKAppleWalkingSteadinessClassificationForQuantity](hkapplewalkingsteadinessclassificationforquantity.md)
  Provides a classification for a score that measures the steadiness of the user’s gait.
- [HKAppleWalkingSteadinessMaximumQuantityForClassification](hkapplewalkingsteadinessmaximumquantityforclassification.md)
  Returns the maximum score for the steadiness of the user’s gait based on the provided classification.
- [HKAppleWalkingSteadinessMinimumQuantityForClassification](hkapplewalkingsteadinessminimumquantityforclassification.md)
  Returns the minimum score for the steadiness of the user’s gait based on the provided classification.
### Attachments
- [class HKAttachment](hkattachment.md)
  A file that is attached to a sample in the HealthKit store.
- [class HKAttachmentStore](hkattachmentstore.md)
  The access point for attachments associated with samples in the HealthKit store.
- [class HKAttachmentDataReader](hkattachmentdatareader.md)
  A reader that provides access to an attachment’s data.
### Digital signatures
- [Adding Digital Signatures](adding-digital-signatures.md)
  Cryptographically sign samples.
### Abstract superclasses
- [class HKQuantitySample](hkquantitysample.md)
  A sample that represents a quantity, including the value and the units.
- [class HKSample](hksample.md)
  A HealthKit sample represents a piece of data associated with a start and end time.
- [class HKObject](hkobject.md)
  A piece of data that can be stored inside the HealthKit store.
### Deprecated classes
- [class HKCumulativeQuantitySeriesSample](hkcumulativequantityseriessample.md)
  A sample representing a series of cumulative quantity values.

## See Also

- [Saving data to HealthKit](saving-data-to-healthkit.md)
  Create and share HealthKit samples.
- [Reading data from HealthKit](reading-data-from-healthkit.md)
  Use queries to request sample data from HealthKit.
- [class HKHealthStore](hkhealthstore.md)
  The access point for all data managed by HealthKit.
- [Creating a Mobility Health App](creating-a-mobility-health-app.md)
  Create a health app that allows a clinical care team to send and receive mobility data.
- [Data types](data-types.md)
  Specify the kind of data used in HealthKit.
- [Queries](queries.md)
  Query health and fitness data.
- [Visualizing HealthKit State of Mind in visionOS](visualizing-healthkit-state-of-mind-in-visionos.md)
  Incorporate HealthKit State of Mind into your app and visualize the data in visionOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/samples)*