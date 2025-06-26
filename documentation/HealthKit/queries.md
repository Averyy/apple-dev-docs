# Queries

**Framework**: HealthKit

Query health and fitness data.

#### Overview

Use queries to read sample data from the HealthKit store. You can also use queries to list all the sources for a particular data type, or to perform statistical calculations for a data type. For example, statistical queries can calculate the minimum and maximum heart rate for a given week, or the total step count for a given day.

You run a query by calling the HealthKit store’s [`execute(_:)`](hkhealthstore/execute(_:).md) method. HealthKit returns a snapshot of the current results to the query’s results handler. Long-running queries continue to monitor the HealthKit store, and return any relevant changes to the query’s update handler. To return sorted or filtered results, give the query a sort descriptor or predicate.

## Topics

### Essentials
- [Reading data from HealthKit](reading-data-from-healthkit.md)
  Use queries to request sample data from HealthKit.
### Swift concurrency support
- [Running Queries with Swift Concurrency](running-queries-with-swift-concurrency.md)
  Use Swift concurrency to manage one-shot and long-running queries.
- [protocol HKAsyncQuery](hkasyncquery.md)
  A protocol that defines an asynchronous method for running queries.
- [protocol HKAsyncSequenceQuery](hkasyncsequencequery.md)
  A protocol that defines a method for running queries that returns results using an asynchronous sequence.
- [struct HKSamplePredicate](hksamplepredicate.md)
  A predicate for queries that return a collection of matching sample objects.
### Basic queries
- [struct HKSampleQueryDescriptor](hksamplequerydescriptor.md)
  A query interface that reads samples using Swift concurrency.
- [class HKSampleQuery](hksamplequery.md)
  A general query that returns a snapshot of all the matching samples currently saved in the HealthKit store.
- [class HKCorrelationQuery](hkcorrelationquery.md)
  A query that performs complex searches based on the correlation’s contents, and returns a snapshot of all matching samples.
- [class HKQueryDescriptor](hkquerydescriptor.md)
  A descriptor that specifies a set of samples based on the data type and a predicate.
- [class HKQuery](hkquery.md)
  An abstract class for all the query classes in HealthKit.
### Series queries
- [struct HKQuantitySeriesSampleQueryDescriptor](hkquantityseriessamplequerydescriptor.md)
  A query interface that reads the series data associated with quantity samples using Swift concurrency.
- [class HKQuantitySeriesSampleQuery](hkquantityseriessamplequery.md)
  A query that accesses the series data associated with a quantity sample.
- [struct HKWorkoutRouteQueryDescriptor](hkworkoutroutequerydescriptor.md)
  A query interface that reads the location data stored in a workout route using Swift concurrency.
- [class HKWorkoutRouteQuery](hkworkoutroutequery.md)
  A query to access the location data stored in a workout route.
- [struct HKHeartbeatSeriesQueryDescriptor](hkheartbeatseriesquerydescriptor.md)
  A query interface that reads the heartbeat series data stored in a heartbeat sample using Swift concurrency.
- [class HKHeartbeatSeriesQuery](hkheartbeatseriesquery.md)
  A query that returns the heartbeat data contained in a heartbeat series sample.
- [struct HKElectrocardiogramQueryDescriptor](hkelectrocardiogramquerydescriptor.md)
  A query interface that reads the underlying voltage measurements for an electrocardiogram sample using Swift concurrency.
- [class HKElectrocardiogramQuery](hkelectrocardiogramquery.md)
  A query that returns the underlying voltage measurements for an electrocardiogram sample.
- [class HKWorkoutEffortRelationship](hkworkouteffortrelationship.md)
- [class HKWorkoutEffortRelationshipQuery](hkworkouteffortrelationshipquery.md)
### Long-running queries
- [struct HKActivitySummaryQueryDescriptor](hkactivitysummaryquerydescriptor.md)
  A query interface that reads activity summaries using Swift concurrency.
- [class HKActivitySummaryQuery](hkactivitysummaryquery.md)
  A query for reading activity summary objects from the HealthKit store.
- [struct HKAnchoredObjectQueryDescriptor](hkanchoredobjectquerydescriptor.md)
  A query interface that runs anchored object queries using Swift concurrency.
- [class HKAnchoredObjectQuery](hkanchoredobjectquery.md)
  A query that returns changes to the HealthKit store, including a snapshot of new changes and continuous monitoring as a long-running query.
- [class HKObserverQuery](hkobserverquery.md)
  A long-running query that monitors the HealthKit store and updates your app when the HealthKit store saves or deletes a matching sample.
### Sources and devices
- [struct HKSourceQueryDescriptor](hksourcequerydescriptor.md)
  A query interface that uses Swift concurrency to read the apps and devices that produced the matching samples.
- [class HKSourceRevision](hksourcerevision.md)
  An object indicating the source of a HealthKit sample.
- [class HKSource](hksource.md)
  An object indicating the app or device that created a HealthKit sample
- [class HKDevice](hkdevice.md)
  A device that generates data for HealthKit.
- [class HKSourceQuery](hksourcequery.md)
  A query that returns a list of sources, such as apps and devices, that have saved matching queries to the HealthKit store.
### Statistics
- [Executing Statistical Queries](executing-statistical-queries.md)
  Create and run statistical queries.
- [Executing Statistics Collection Queries](executing-statistics-collection-queries.md)
  Calculate statistical data for graphs and charts.
- [struct HKStatisticsQueryDescriptor](hkstatisticsquerydescriptor.md)
  A query descriptor that calculates the minimum, maximum, average, or sum over a set of samples from the HealthKit store.
- [class HKStatisticsQuery](hkstatisticsquery.md)
  A query that performs statistical calculations over a set of matching quantity samples, and returns the results.
- [struct HKStatisticsCollectionQueryDescriptor](hkstatisticscollectionquerydescriptor.md)
  A query descriptor that gathers a collection of statistics calculated over a series of fixed-length time intervals.
- [class HKStatisticsCollectionQuery](hkstatisticscollectionquery.md)
  A query that performs multiple statistics queries over a series of fixed-length time intervals.
- [class HKStatistics](hkstatistics.md)
  An object that represents the result of calculating the minimum, maximum, average, or sum over a set of samples from the HealthKit store.
- [class HKStatisticsCollection](hkstatisticscollection.md)
  An object that manages a collection of statistics, representing the results calculated over separate time intervals.
- [struct HKStatisticsOptions](hkstatisticsoptions.md)
  Options for specifying the statistic to calculate.
### Clinical record queries
- [struct HKVerifiableClinicalRecordQueryDescriptor](hkverifiableclinicalrecordquerydescriptor.md)
  A query interface that provides one-time access to a SMART Health Card or EU Digital COVID Certificate using Swift concurrency.
- [class HKVerifiableClinicalRecordQuery](hkverifiableclinicalrecordquery.md)
  A query for one-time access to a SMART Health Card or EU Digital COVID Certificate.
- [struct HKVerifiableClinicalRecordSourceType](hkverifiableclinicalrecordsourcetype.md)
  The source type for the verifiable clinical record.
- [struct HKVerifiableClinicalRecordCredentialType](hkverifiableclinicalrecordcredentialtype.md)
  The type of record returned by a verifiable clinical record query.
- [class HKDocumentQuery](hkdocumentquery.md)
  A query that returns a snapshot of all matching documents currently saved in the HealthKit store.
### Medication queries
- [class HKClinicalCoding](hkclinicalcoding.md)
- [class HKHealthConceptIdentifier](hkhealthconceptidentifier.md)
- [class HKMedicationConcept](hkmedicationconcept.md)
- [class HKMedicationDoseEvent](hkmedicationdoseevent.md)
- [class HKMedicationDoseEventType](hkmedicationdoseeventtype.md)
- [class HKUserAnnotatedMedication](hkuserannotatedmedication.md)
- [class HKUserAnnotatedMedicationQuery](hkuserannotatedmedicationquery.md)
- [class HKUserAnnotatedMedicationType](hkuserannotatedmedicationtype.md)
- [struct HKHealthConceptDomain](hkhealthconceptdomain.md)
  Represents the domain of a HKHealthConceptIdentifier
- [struct HKMedicationGeneralForm](hkmedicationgeneralform.md)
  Represents a medications general form.
- [struct HKUserAnnotatedMedicationQueryDescriptor](hkuserannotatedmedicationquerydescriptor.md)

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
- [Samples](samples.md)
  Create and save health and fitness samples.
- [Visualizing HealthKit State of Mind in visionOS](visualizing-healthkit-state-of-mind-in-visionos.md)
  Incorporate HealthKit State of Mind into your app and visualize the data in visionOS.
- [Logging symptoms associated with a medication](logging-symptoms-associated-with-a-medication.md)
  Fetch medications and dose events from the HealthKit store, and create symptom samples to associate with them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/queries)*