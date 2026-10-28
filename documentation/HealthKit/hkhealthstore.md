# HKHealthStore

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

The access point for all data managed by HealthKit.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKHealthStore
```

```objc
@interface HKHealthStore : NSObject
```

## Mentions

- [Executing Observer Queries](./executing-observer-queries.md)
- [Reading data from HealthKit](./reading-data-from-healthkit.md)

## Overview

Use a [`HKHealthStore`](./hkhealthstore.md) object to request permission to share or read HealthKit data. People can grant your app full access to a data type, limited access restricted to a recent window of data, or no access at all. After requesting authorization, you can check the scope of your read access for specific data types before making queries. You can also use the HealthKit store to save new samples to the store, manage the samples that your app saves, and start, stop, and manage queries.

For more information, see [Setting up HealthKit](./setting-up-healthkit.md).

## Topics

### Accessing HealthKit
- [func authorizationStatus(for: HKObjectType) -> HKAuthorizationStatus](./hkhealthstore/authorizationstatus%28for%29.md)
  Returns the app’s authorization status for sharing the specified data type.
- [enum HKAuthorizationStatus](./hkauthorizationstatus.md)
  Constants indicating the authorization status for a particular data type.
- [func getRequestStatusForAuthorization(toShare: Set<HKSampleType>, read: Set<HKObjectType>, completion: (HKAuthorizationRequestStatus, (any Error)?) -> Void)](./hkhealthstore/getrequeststatusforauthorization%28toshare,read,completion%29.md)
  Indicates whether the system presents the user with a permission sheet if your app requests authorization for the provided types.
- [enum HKAuthorizationRequestStatus](./hkauthorizationrequeststatus.md)
  Values that indicate whether your app needs to request authorization from the user.
- [class func isHealthDataAvailable() -> Bool](./hkhealthstore/ishealthdataavailable%28%29.md)
  Returns a Boolean value that indicates whether HealthKit is available on this device.
- [func supportsHealthRecords() -> Bool](./hkhealthstore/supportshealthrecords%28%29.md)
  Returns a Boolean value that indicates whether the current device supports clinical records.
- [func requestAuthorization(toShare: Set<HKSampleType>?, read: Set<HKObjectType>?, completion: (Bool, (any Error)?) -> Void)](./hkhealthstore/requestauthorization%28toshare,read,completion%29.md)
  Requests permission to save and read the specified data types.
- [func requestAuthorization(toShare: Set<HKSampleType>, read: Set<HKObjectType>) async throws](./hkhealthstore/requestauthorization%28toshare,read%29.md)
  Asynchronously requests permission to save and read the specified data types.
- [func requestPerObjectReadAuthorization(for: HKObjectType, predicate: NSPredicate?, completion: (Bool, (any Error)?) -> Void)](./hkhealthstore/requestperobjectreadauthorization%28for,predicate,completion%29.md)
  Asynchronously requests permission to read a data type that requires per-object authorization (such as vision prescriptions).
- [func handleAuthorizationForExtension(completion: (Bool, (any Error)?) -> Void)](./hkhealthstore/handleauthorizationforextension%28completion%29.md)
  Requests permission to save and read the data types specified by an extension.
- [var authorizationViewControllerPresenter: UIViewController?](./hkhealthstore/authorizationviewcontrollerpresenter.md)
  The view controller that presents HealthKit authorization sheets.
- [func getEarliestAuthorizedSampleDate(for: Set<HKObjectType>, completion: ([HKObjectType : Date]?, (any Error)?) -> Void)](./hkhealthstore/getearliestauthorizedsampledate%28for,completion%29.md)
  Returns the earliest date that the person permits your app to read samples for the given data types.
- [func earliestPermittedSampleDate() -> Date](./hkhealthstore/earliestpermittedsampledate%28%29.md)
  Returns the earliest date that the framework permits your app to save or read samples.
### Querying HealthKit data
- [func execute(HKQuery)](./hkhealthstore/execute%28_%29.md)
  Starts executing the provided query.
- [func stop(HKQuery)](./hkhealthstore/stop%28_%29.md)
  Stops a long-running query.
### Reading characteristic data
- [func biologicalSex() throws -> HKBiologicalSexObject](./hkhealthstore/biologicalsex%28%29.md)
  Reads someone’s biological sex from the HealthKit store.
- [func bloodType() throws -> HKBloodTypeObject](./hkhealthstore/bloodtype%28%29.md)
  Reads the user’s blood type from the HealthKit store.
- [func dateOfBirth() throws -> Date](./hkhealthstore/dateofbirth%28%29.md)
  Reads the user’s date of birth from the HealthKit store as a date value.
- [func dateOfBirthComponents() throws -> DateComponents](./hkhealthstore/dateofbirthcomponents%28%29.md)
  Reads the user’s date of birth from the HealthKit store as date components.
- [func fitzpatrickSkinType() throws -> HKFitzpatrickSkinTypeObject](./hkhealthstore/fitzpatrickskintype%28%29.md)
  Reads the user’s Fitzpatrick Skin Type from the HealthKit store.
- [func wheelchairUse() throws -> HKWheelchairUseObject](./hkhealthstore/wheelchairuse%28%29.md)
  Reads the user’s wheelchair use from the HealthKit store.
### Working with HealthKit objects
- [func delete(HKObject, withCompletion: (Bool, (any Error)?) -> Void)](./hkhealthstore/delete%28_,withcompletion%29-78l1m.md)
  Deletes the specified object from the HealthKit store.
- [func delete([HKObject], withCompletion: (Bool, (any Error)?) -> Void)](./hkhealthstore/delete%28_,withcompletion%29-17hzm.md)
  Deletes the specified objects from the HealthKit store.
- [func deleteObjects(of: HKObjectType, predicate: NSPredicate, withCompletion: (Bool, Int, (any Error)?) -> Void)](./hkhealthstore/deleteobjects%28of,predicate,withcompletion%29.md)
  Deletes objects saved by this application that match the provided type and predicate.
- [func save(HKObject, withCompletion: (Bool, (any Error)?) -> Void)](./hkhealthstore/save%28_,withcompletion%29-6fmtg.md)
  Saves the provided object to the HealthKit store.
- [func save([HKObject], withCompletion: (Bool, (any Error)?) -> Void)](./hkhealthstore/save%28_,withcompletion%29-47iwb.md)
  Saves an array of objects to the HealthKit store.
### Accessing the preferred units
- [func preferredUnits(for: Set<HKQuantityType>, completion: ([HKQuantityType : HKUnit], (any Error)?) -> Void)](./hkhealthstore/preferredunits%28for,completion%29.md)
  Returns the user’s preferred units for the given quantity types.
- [func preferredWorkoutZoneConfiguration(for: HKQuantityType) async throws -> HKWorkoutZoneConfiguration?](./hkhealthstore/preferredworkoutzoneconfiguration%28for%29.md)
  Returns a person’s preferred zone configuration for a quantity type.
- [static let HKUserPreferencesDidChange: NSNotification.Name](../Foundation/nsnotification/name-swift.struct/hkuserpreferencesdidchange.md)
  Notifies observers whenever the user changes his or her preferred units.
- [HKUserPreferencesDidChangeNotification](./hkuserpreferencesdidchangenotification.md)
  Notifies observers whenever the user changes his or her preferred units.
### Managing background delivery
- [func enableBackgroundDelivery(for: HKObjectType, frequency: HKUpdateFrequency, withCompletion: (Bool, (any Error)?) -> Void)](./hkhealthstore/enablebackgrounddelivery%28for,frequency,withcompletion%29.md)
  Enables the delivery of updates to an app running in the background.
- [com.apple.developer.healthkit.background-delivery](../BundleResources/entitlements/com.apple.developer.healthkit.background-delivery.md)
  A Boolean value that indicates whether observer queries receive updates while running in the background.
- [enum HKUpdateFrequency](./hkupdatefrequency.md)
  Constants that determine how often the system launches your app in response to changes to HealthKit data.
- [func disableBackgroundDelivery(for: HKObjectType, withCompletion: (Bool, (any Error)?) -> Void)](./hkhealthstore/disablebackgrounddelivery%28for,withcompletion%29.md)
  Disables background deliveries of update notifications for the specified data type.
- [func disableAllBackgroundDelivery(completion: (Bool, (any Error)?) -> Void)](./hkhealthstore/disableallbackgrounddelivery%28completion%29.md)
  Disables all background deliveries of update notifications.
### Managing workouts
- [func splitTotalEnergy(HKQuantity, start: Date, end: Date, resultsHandler: (HKQuantity?, HKQuantity?, (any Error)?) -> Void)](./hkhealthstore/splittotalenergy%28_,start,end,resultshandler%29.md)
  Calculates the active and resting energy burned based on the total energy burned over the given duration.
- [func recoverActiveWorkoutSession(completion: (HKWorkoutSession?, (any Error)?) -> Void)](./hkhealthstore/recoveractiveworkoutsession%28completion%29.md)
  Recovers an active workout session.
### Managing workout sessions
- [var workoutSessionMirroringStartHandler: ((HKWorkoutSession) -> Void)?](./hkhealthstore/workoutsessionmirroringstarthandler.md)
  A block that the system calls when it starts a mirrored workout session.
- [func startWatchApp(with: HKWorkoutConfiguration, completion: (Bool, (any Error)?) -> Void)](./hkhealthstore/startwatchapp%28with,completion%29.md)
  Launches or wakes the companion watchOS app to create a new workout session.
- [func pause(HKWorkoutSession)](./hkhealthstore/pause%28_%29.md)
  Pauses the provided workout session.
- [func resumeWorkoutSession(HKWorkoutSession)](./hkhealthstore/resumeworkoutsession%28_%29.md)
  Resumes the provided workout session.
### Managing estimates
- [func recalibrateEstimates(sampleType: HKSampleType, date: Date, completion: (Bool, (any Error)?) -> Void)](./hkhealthstore/recalibrateestimates%28sampletype,date,completion%29.md)
  Recalibrates the prediction algorithm used to calculate the specified sample type.
### Accessing the move mode
- [func activityMoveMode() throws -> HKActivityMoveModeObject](./hkhealthstore/activitymovemode%28%29.md)
  Returns the activity move mode for the current user.
- [static let HKUserPreferencesDidChange: NSNotification.Name](../Foundation/nsnotification/name-swift.struct/hkuserpreferencesdidchange.md)
  Notifies observers whenever the user changes his or her preferred units.
### Deprecated symbols
- [func add([HKSample], to: HKWorkout, completion: (Bool, (any Error)?) -> Void)](./hkhealthstore/add%28_,to,completion%29.md)
  Associates the provided samples with the specified workout.
- [func start(HKWorkoutSession)](./hkhealthstore/start%28_%29.md)
  Starts a workout session for the current app.
- [func end(HKWorkoutSession)](./hkhealthstore/end%28_%29.md)
  Ends a workout session for the current app.
### Structures
- [HKHealthStore.HKUserPreferencesDidChangeMessage](./hkhealthstore/hkuserpreferencesdidchangemessage.md)
### Instance Methods
- [func relateWorkoutEffortSample(HKSample, with: HKWorkout, activity: HKWorkoutActivity?, completion: (Bool, (any Error)?) -> Void)](./hkhealthstore/relateworkouteffortsample%28_,with,activity,completion%29.md)
- [func unrelateWorkoutEffortSample(HKSample, from: HKWorkout, activity: HKWorkoutActivity?, completion: (Bool, (any Error)?) -> Void)](./hkhealthstore/unrelateworkouteffortsample%28_,from,activity,completion%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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

### Health data
- [Saving data to HealthKit](./saving-data-to-healthkit.md)
  Create and share HealthKit samples.
- [Reading data from HealthKit](./reading-data-from-healthkit.md)
  Use queries to request sample data from HealthKit.
- [Creating a Mobility Health App](./creating-a-mobility-health-app.md)
  Create a health app that allows a clinical care team to send and receive mobility data.
- [Data types](./data-types.md)
  Specify the kind of data used in HealthKit.
- [Samples](./samples.md)
  Create and save health and fitness samples.
- [Queries](./queries.md)
  Query health and fitness data.
- [Visualizing HealthKit State of Mind in visionOS](./visualizing-healthkit-state-of-mind-in-visionos.md)
  Incorporate HealthKit State of Mind into your app and visualize the data in visionOS.
- [Logging symptoms associated with a medication](./logging-symptoms-associated-with-a-medication.md)
  Fetch medications and dose events from the HealthKit store, and create symptom samples to associate with them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore)*