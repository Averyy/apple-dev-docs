# CMHeadphoneActivityManager

**Framework**: Core Motion  
**Kind**: class

An object that starts and manages headphone activity services.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 11.0+

## Declaration

```swift
class CMHeadphoneActivityManager
```

#### Overview

This class delivers headphone activity updates to your app. Use an instance of the manager to determine if the device supports headphone activity updates, and to start and stop updates. Before using this class, check [`isActivityAvailable`](cmheadphoneactivitymanager/isactivityavailable.md) and [`isStatusAvailable`](cmheadphoneactivitymanager/isstatusavailable.md) to make sure the features are available.

This class provides similar information to [`CMMotionActivityManager`](cmmotionactivitymanager.md), except the activity information comes from headphone motion, rather than from device motion.

> ❗ **Important**:  In iOS and macOS, include the [`NSMotionUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMotionUsageDescription) key in your app’s `Info.plist` file. If this key is absent, trying to start headphone activity updates terminates your app.

 In iOS and macOS, include the [`NSMotionUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMotionUsageDescription) key in your app’s `Info.plist` file. If this key is absent, trying to start headphone activity updates terminates your app.

## Topics

### Checking Availability
- [var isActivityAvailable: Bool](cmheadphoneactivitymanager/isactivityavailable.md)
  A Boolean value that indicates whether the current device supports headphone activity.
- [var isActivityActive: Bool](cmheadphoneactivitymanager/isactivityactive.md)
  A Boolean value that indicates whether headphone motion activity is active.
- [var isStatusAvailable: Bool](cmheadphoneactivitymanager/isstatusavailable.md)
  A Boolean value that indicates whether the current device supports headphone status.
- [var isStatusActive: Bool](cmheadphoneactivitymanager/isstatusactive.md)
  A Boolean value that indicates whether headphone status is active.
- [class func authorizationStatus() -> CMAuthorizationStatus](cmheadphoneactivitymanager/authorizationstatus.md)
  Returns the authorization status for monitoring headphone activity.
### Starting and Stopping Updates
- [func startActivityUpdates(to: OperationQueue, withHandler: CMHeadphoneActivityManager.ActivityHandler)](cmheadphoneactivitymanager/startactivityupdates(to:withhandler:).md)
  Starts headphone activity updates, providing data to the given handler through the given queue.
- [func stopActivityUpdates()](cmheadphoneactivitymanager/stopactivityupdates.md)
  Stops headphone activity updates.
- [func startStatusUpdates(to: OperationQueue, withHandler: CMHeadphoneActivityManager.StatusHandler)](cmheadphoneactivitymanager/startstatusupdates(to:withhandler:).md)
  Starts headphone status updates, providing data to the given handler through the given queue.
- [func stopStatusUpdates()](cmheadphoneactivitymanager/stopstatusupdates.md)
  Stops headphone status updates.
### Supporting Types
- [CMHeadphoneActivityManager.Status](cmheadphoneactivitymanager/status.md)
  Headphone connection status updates.
- [CMHeadphoneActivityManager.ActivityHandler](cmheadphoneactivitymanager/activityhandler.md)
  The type for a handler to be invoked when headphone motion activity data is available.
- [CMHeadphoneActivityManager.StatusHandler](cmheadphoneactivitymanager/statushandler.md)
  The type for a handler to be invoked with status updates.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CMMotionActivityManager](cmmotionactivitymanager.md)
  An object that manages access to the motion data stored by the device.
- [class CMMotionActivity](cmmotionactivity.md)
  The data for a single motion update event.
- [Getting motion-activity data from headphones](getting-motion-activity-data-from-headphones.md)
  Configure your app to listen for motion-activity changes from headphones.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager)*