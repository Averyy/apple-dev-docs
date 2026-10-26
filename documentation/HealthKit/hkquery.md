# HKQuery

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

An abstract class for all the query classes in HealthKit.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKQuery
```

```objc
@interface HKQuery : NSObject
```

## Mentions

- [Dividing a HealthKit workout into activities](./dividing-a-healthkit-workout-into-activities.md)

#### Overview

The [`HKQuery`](./hkquery.md) class is the basis for all the query objects that retrieve data from the HealthKit store. The [`HKQuery`](./hkquery.md) class is an abstract class. You should never instantiate it directly. Instead, you always work with one of its concrete subclasses.

##### Filter queries using predicates

All the concrete `HKQuery` subclasses take a predicate. You can use this predicate to filter the samples returned by the query. When HealthKit runs a query, it converts the predicate to SQL and executes the SQL on the underlying store. This has two important side effects.

- Predicates improve the performance of your query, both in terms of speed and memory usage. Because the store executes the predicate, it restricts the number of HealthKit objects that it instantiates and returns.
- Since the store executes these predicates, it limits the type of predicates that you can use. Specifically, HealthKit provides several predicate key paths (for example, [`HKPredicateKeyPathUUID`](./hkpredicatekeypathuuid.md) and [`HKPredicateKeyPathMetadata`](./hkpredicatekeypathmetadata.md)). You can create predicates using only these key paths.

## Topics

### Accessing properties
- [var predicate: NSPredicate?](./hkquery/predicate.md)
  A predicate used to filter the objects returned from the HealthKit store.
- [var objectType: HKObjectType?](./hkquery/objecttype.md)
  The type of objects being queried.
- [var sampleType: HKSampleType?](./hkquery/sampletype.md)
  The type of objects being queried.
### Creating object predicates
- [class func predicateForObject(with: UUID) -> NSPredicate](./hkquery/predicateforobject%28with%29.md)
  Returns a predicate that matches an object with the specified universally unique identifier (UUID).
- [class func predicateForObjects(with: Set<UUID>) -> NSPredicate](./hkquery/predicateforobjects%28with%29.md)
  Returns a predicate that matches the objects with the specified  universally unique identifiers (UUIDs).
- [class func predicateForObjects(from: HKSource) -> NSPredicate](./hkquery/predicateforobjects%28from%29-7j3p2.md)
  Returns a predicate that matches all the objects that were created by the provided source.
- [class func predicateForObjects(from: Set<HKSource>) -> NSPredicate](./hkquery/predicateforobjects%28from%29-89b4t.md)
  Returns a predicate that matches all the objects that were created by any of the provided sources.
- [class func predicateForObjects(from: Set<HKDevice>) -> NSPredicate](./hkquery/predicateforobjects%28from%29-9h87f.md)
  Returns a predicate that matches all the objects that were created by any of the provided devices.
- [class func predicateForObjects(withDeviceProperty: String, allowedValues: Set<String>) -> NSPredicate](./hkquery/predicateforobjects%28withdeviceproperty,allowedvalues%29.md)
  Returns a predicate that matches all objects created by devices with the specified properties.
- [class func predicateForObjects(from: Set<HKSourceRevision>) -> NSPredicate](./hkquery/predicateforobjects%28from%29-1ar4g.md)
  Returns a predicate that matches all the objects that were created by any of the provided source revisions.
- [class func predicateForObjects(withMetadataKey: String) -> NSPredicate](./hkquery/predicateforobjects%28withmetadatakey%29.md)
  Returns a predicate that matches any object whose metadata contains the provided key.
- [class func predicateForObjects(withMetadataKey: String, allowedValues: [Any]) -> NSPredicate](./hkquery/predicateforobjects%28withmetadatakey,allowedvalues%29.md)
  Returns a predicate that matches objects based on the provided metadata key and an array of target values.
- [class func predicateForObjects(withMetadataKey: String, operatorType: NSComparisonPredicate.Operator, value: Any) -> NSPredicate](./hkquery/predicateforobjects%28withmetadatakey,operatortype,value%29.md)
  Returns a predicate that matches objects based on the provided metadata key, value, and operator.
- [class func predicateForObjectsWithNoCorrelation() -> NSPredicate](./hkquery/predicateforobjectswithnocorrelation%28%29.md)
  Returns a predicate that matches all objects that are not associated with a HealthKit correlation.
### Creating sample predicates
- [class func predicateForSamples(withStart: Date?, end: Date?, options: HKQueryOptions) -> NSPredicate](./hkquery/predicateforsamples%28withstart,end,options%29.md)
  Returns a predicate for samples whose start and end dates fall within the specified time interval.
- [struct HKQueryOptions](./hkqueryoptions.md)
  Constants that describe how a sample’s time period overlaps with the target time period.
### Creating quantity sample predicates
- [class func predicateForQuantitySamples(with: NSComparisonPredicate.Operator, quantity: HKQuantity) -> NSPredicate](./hkquery/predicateforquantitysamples%28with,quantity%29.md)
  Returns a predicate that matches samples based on the target quantity.
### Creating category sample predicates
- [class func predicateForCategorySamples(with: NSComparisonPredicate.Operator, value: Int) -> NSPredicate](./hkquery/predicateforcategorysamples%28with,value%29.md)
  Returns a predicate that checks a category sample’s value.
- [protocol HKCategoryValuePredicateProviding](./hkcategoryvaluepredicateproviding.md)
  A protocol for objects that produce predicates that match category value samples.
- [+ predicateForCategorySamplesEqualToValues:](./hkquery/predicateforcategorysamplesequaltovalues_.md)
  A predicate that returns category samples with a matching value.
### Creating clinical record predicates
- [class func predicateForClinicalRecords(from: HKSource, fhirResourceType: HKFHIRResourceType, identifier: String) -> NSPredicate](./hkquery/predicateforclinicalrecords%28from,fhirresourcetype,identifier%29.md)
  Returns a predicate for a specific FHIR resource.
- [class func predicateForClinicalRecords(withFHIRResourceType: HKFHIRResourceType) -> NSPredicate](./hkquery/predicateforclinicalrecords%28withfhirresourcetype%29.md)
  Returns a predicate for a specific FHIR type.
- [class func predicateForVerifiableClinicalRecords(withRelevantDateWithin: DateInterval) -> NSPredicate](./hkquery/predicateforverifiableclinicalrecords%28withrelevantdatewithin%29.md)
  Returns a predicate that finds verifiable health records with a relevant date within the specified range.
### Creating workout predicates
- [class func predicateForObjects(from: HKWorkout) -> NSPredicate](./hkquery/predicateforobjects%28from%29-5irg9.md)
  Returns a predicate that matches any objects that have been associated with the provided workout.
- [class func predicateForWorkouts(with: HKWorkoutActivityType) -> NSPredicate](./hkquery/predicateforworkouts%28with%29.md)
  Returns a predicate for matching workouts based on the type of activity.
- [class func predicateForWorkouts(activityPredicate: NSPredicate) -> NSPredicate](./hkquery/predicateforworkouts%28activitypredicate%29.md)
  Returns a predicate for matching workouts based on the associated workout activities.
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, duration: TimeInterval) -> NSPredicate](./hkquery/predicateforworkouts%28with,duration%29.md)
  Returns a predicate for matching workouts based on their duration.
- [class func predicateForWorkouts(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, averageQuantity: HKQuantity) -> NSPredicate](./hkquery/predicateforworkouts%28operatortype,quantitytype,averagequantity%29.md)
  Returns a predicate for matching workouts based the average value of an associated quantity type.
- [class func predicateForWorkouts(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, maximumQuantity: HKQuantity) -> NSPredicate](./hkquery/predicateforworkouts%28operatortype,quantitytype,maximumquantity%29.md)
  Returns a predicate for matching workout activities based the maximum value of an associated quantity type.
- [class func predicateForWorkouts(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, minimumQuantity: HKQuantity) -> NSPredicate](./hkquery/predicateforworkouts%28operatortype,quantitytype,minimumquantity%29.md)
  Returns a predicate for matching workout activities based the minimum value of an associated quantity type.
- [class func predicateForWorkouts(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, sumQuantity: HKQuantity) -> NSPredicate](./hkquery/predicateforworkouts%28operatortype,quantitytype,sumquantity%29.md)
  Returns a predicate for matching workout activities based the sum of an associated quantity type.
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, totalDistance: HKQuantity) -> NSPredicate](./hkquery/predicateforworkouts%28with,totaldistance%29.md)
  Returns a predicate for matching workouts based on the total distance traveled.
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, totalEnergyBurned: HKQuantity) -> NSPredicate](./hkquery/predicateforworkouts%28with,totalenergyburned%29.md)
  Returns a predicate for matching workouts based on the total energy burned.
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, totalFlightsClimbed: HKQuantity) -> NSPredicate](./hkquery/predicateforworkouts%28with,totalflightsclimbed%29.md)
  Returns a predicate that matches workout samples based on the number of flights climbed.
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, totalSwimmingStrokeCount: HKQuantity) -> NSPredicate](./hkquery/predicateforworkouts%28with,totalswimmingstrokecount%29.md)
  Returns a predicate that matches workout samples based on the number of strokes while swimming.
### Creating workout activity predicates
- [class func predicateForWorkoutActivities(workoutActivityType: HKWorkoutActivityType) -> NSPredicate](./hkquery/predicateforworkoutactivities%28workoutactivitytype%29.md)
  Returns a predicate for workout activities based on the type of activity performed.
- [class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, duration: TimeInterval) -> NSPredicate](./hkquery/predicateforworkoutactivities%28operatortype,duration%29.md)
  Returns a predicate for matching workout activities based on their duration.
- [class func predicateForWorkoutActivities(start: Date?, end: Date?, options: HKQueryOptions) -> NSPredicate](./hkquery/predicateforworkoutactivities%28start,end,options%29.md)
  Returns a predicate for workout activities that occur between the start and end date.
- [class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, averageQuantity: HKQuantity) -> NSPredicate](./hkquery/predicateforworkoutactivities%28operatortype,quantitytype,averagequantity%29.md)
  Returns a predicate for matching workout activities based the average value of an associated quantity type.
- [class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, maximumQuantity: HKQuantity) -> NSPredicate](./hkquery/predicateforworkoutactivities%28operatortype,quantitytype,maximumquantity%29.md)
  Returns a predicate for matching workout activities based the maximum value of an associated quantity type.
- [class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, minimumQuantity: HKQuantity) -> NSPredicate](./hkquery/predicateforworkoutactivities%28operatortype,quantitytype,minimumquantity%29.md)
  Returns a predicate for matching workout activities based the minimum value of an associated quantity type.
- [class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, sumQuantity: HKQuantity) -> NSPredicate](./hkquery/predicateforworkoutactivities%28operatortype,quantitytype,sumquantity%29.md)
  Returns a predicate for matching workout activities based the sum of an associated quantity type.
### Creating activity summary predicates
- [class func predicateForActivitySummary(with: DateComponents) -> NSPredicate](./hkquery/predicateforactivitysummary%28with%29.md)
  Returns a predicate that matches the activity summary for the specified day.
- [class func predicate(forActivitySummariesBetweenStart: DateComponents, end: DateComponents) -> NSPredicate](./hkquery/predicate%28foractivitysummariesbetweenstart,end%29.md)
  Returns a predicate for matching all the activity summaries that fall between the days identified by the start and end date components.
### Creating electrocardiogram predicates
- [class func predicateForElectrocardiograms(classification: HKElectrocardiogram.Classification) -> NSPredicate](./hkquery/predicateforelectrocardiograms%28classification%29.md)
  Returns a predicate that matches electrocardiogram samples with the specified classification.
- [class func predicateForElectrocardiograms(symptomsStatus: HKElectrocardiogram.SymptomsStatus) -> NSPredicate](./hkquery/predicateforelectrocardiograms%28symptomsstatus%29.md)
  Returns a predicate that matches electrocardiogram samples with the specified symptom status.
- [class func predicateForObjectsAssociated(electrocardiogram: HKElectrocardiogram) -> NSPredicate](./hkquery/predicateforobjectsassociated%28electrocardiogram%29.md)
  Returns a predicate that matches symptom samples associated with the specified electrocardiogram.
### Creating predicate format strings
- [Predicate format strings](./predicate-format-strings.md)
  Formatting strings for creating predicates.
### Creating sort descriptors
- [HealthKit sort descriptors](./healthkit-sort-descriptors.md)
  Identifiers for sorting results.
### Type Methods
- [class func predicateForMedicationDoseEvent(medicationConceptIdentifier: HKHealthConceptIdentifier) -> NSPredicate](./hkquery/predicateformedicationdoseevent%28medicationconceptidentifier%29.md)
- [class func predicateForMedicationDoseEvent(medicationConceptIdentifiers: Set<HKHealthConceptIdentifier>) -> NSPredicate](./hkquery/predicateformedicationdoseevent%28medicationconceptidentifiers%29.md)
- [class func predicateForMedicationDoseEvent(scheduledDate: Date) -> NSPredicate](./hkquery/predicateformedicationdoseevent%28scheduleddate%29.md)
- [class func predicateForMedicationDoseEvent(scheduledDates: Set<Date>) -> NSPredicate](./hkquery/predicateformedicationdoseevent%28scheduleddates%29.md)
- [class func predicateForMedicationDoseEvent(scheduledStart: Date?, end: Date?) -> NSPredicate](./hkquery/predicateformedicationdoseevent%28scheduledstart,end%29.md)
- [class func predicateForMedicationDoseEvent(status: HKMedicationDoseEvent.LogStatus) -> NSPredicate](./hkquery/predicateformedicationdoseevent%28status%29.md)
- [class func predicateForMedicationDoseEvent(statuses: Set<NSNumber>) -> NSPredicate](./hkquery/predicateformedicationdoseevent%28statuses%29.md)
- [class func predicateForStatesOfMind(with: HKStateOfMind.Label) -> NSPredicate](./hkquery/predicateforstatesofmind%28with%29-3iyym.md)
- [class func predicateForStatesOfMind(with: HKStateOfMind.Kind) -> NSPredicate](./hkquery/predicateforstatesofmind%28with%29-6obe4.md)
- [class func predicateForStatesOfMind(with: HKStateOfMind.Association) -> NSPredicate](./hkquery/predicateforstatesofmind%28with%29-9fny6.md)
- [class func predicateForStatesOfMind(withValence: Double, operatorType: NSComparisonPredicate.Operator) -> NSPredicate](./hkquery/predicateforstatesofmind%28withvalence,operatortype%29.md)
- [class func predicateForUserAnnotatedMedications(hasSchedule: Bool) -> NSPredicate](./hkquery/predicateforuserannotatedmedications%28hasschedule%29.md)
- [class func predicateForUserAnnotatedMedications(isArchived: Bool) -> NSPredicate](./hkquery/predicateforuserannotatedmedications%28isarchived%29.md)
- [class func predicateForWorkoutEffortSamplesRelated(workout: HKWorkout, activity: HKWorkoutActivity?) -> NSPredicate](./hkquery/predicateforworkouteffortsamplesrelated%28workout,activity%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [HKActivitySummaryQuery](./hkactivitysummaryquery.md)
- [HKAnchoredObjectQuery](./hkanchoredobjectquery.md)
- [HKCorrelationQuery](./hkcorrelationquery.md)
- [HKDocumentQuery](./hkdocumentquery.md)
- [HKElectrocardiogramQuery](./hkelectrocardiogramquery.md)
- [HKHeartbeatSeriesQuery](./hkheartbeatseriesquery.md)
- [HKObserverQuery](./hkobserverquery.md)
- [HKQuantitySeriesSampleQuery](./hkquantityseriessamplequery.md)
- [HKSampleQuery](./hksamplequery.md)
- [HKSourceQuery](./hksourcequery.md)
- [HKStatisticsCollectionQuery](./hkstatisticscollectionquery.md)
- [HKStatisticsQuery](./hkstatisticsquery.md)
- [HKUserAnnotatedMedicationQuery](./hkuserannotatedmedicationquery.md)
- [HKVerifiableClinicalRecordQuery](./hkverifiableclinicalrecordquery.md)
- [HKWorkoutEffortRelationshipQuery](./hkworkouteffortrelationshipquery.md)
- [HKWorkoutRouteQuery](./hkworkoutroutequery.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Related Documentation
- [class HKActivitySummaryQuery](./hkactivitysummaryquery.md)
  A query for reading activity summary objects from the HealthKit store.
- [class HKAnchoredObjectQuery](./hkanchoredobjectquery.md)
  A query that returns changes to the HealthKit store, including a snapshot of new changes and continuous monitoring as a long-running query.
- [class HKDocumentQuery](./hkdocumentquery.md)
  A query that returns a snapshot of all matching documents currently saved in the HealthKit store.
- [class HKObserverQuery](./hkobserverquery.md)
  A long-running query that monitors the HealthKit store and updates your app when the HealthKit store saves or deletes a matching sample.
- [class HKSourceQuery](./hksourcequery.md)
  A query that returns a list of sources, such as apps and devices, that have saved matching queries to the HealthKit store.
- [class HKStatisticsQuery](./hkstatisticsquery.md)
  A query that performs statistical calculations over a set of matching quantity samples, and returns the results.
- [class HKStatisticsCollectionQuery](./hkstatisticscollectionquery.md)
  A query that performs multiple statistics queries over a series of fixed-length time intervals.
- [class HKWorkoutRouteQuery](./hkworkoutroutequery.md)
  A query to access the location data stored in a workout route.
### Basic queries
- [struct HKSampleQueryDescriptor](./hksamplequerydescriptor.md)
  A query interface that reads samples using Swift concurrency.
- [class HKSampleQuery](./hksamplequery.md)
  A general query that returns a snapshot of all the matching samples currently saved in the HealthKit store.
- [class HKCorrelationQuery](./hkcorrelationquery.md)
  A query that performs complex searches based on the correlation’s contents, and returns a snapshot of all matching samples.
- [class HKQueryDescriptor](./hkquerydescriptor.md)
  A descriptor that specifies a set of samples based on the data type and a predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery)*