# CMMotionActivityManager

**Framework**: Core Motion  
**Kind**: class

An object that manages access to the motion data stored by the device.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
class CMMotionActivityManager
```

#### Overview

Motion data reflects whether the user is walking, running, in a vehicle, or stationary for periods of time. Using this class, you can ask for notifications when the current type of motion changes or you can gather past motion change data. For example, a navigation app might look for changes in the current type of motion and offer different directions for each.

> ❗ **Important**:  To use this API, you must include the [`NSMotionUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMotionUsageDescription) key in your app’s `Info.plist` file and provide a usage description string for this key. The usage description appears in the prompt that the user must accept the first time the system asks the user to access motion data for your app. If you don’t include a usage description string, your app crashes when you call this API.

 To use this API, you must include the [`NSMotionUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMotionUsageDescription) key in your app’s `Info.plist` file and provide a usage description string for this key. The usage description appears in the prompt that the user must accept the first time the system asks the user to access motion data for your app. If you don’t include a usage description string, your app crashes when you call this API.

## Topics

### Determining Activity Availability
- [class func isActivityAvailable() -> Bool](cmmotionactivitymanager/isactivityavailable.md)
  Returns a Boolean indicating whether motion data is available on the current device.
- [class func authorizationStatus() -> CMAuthorizationStatus](cmmotionactivitymanager/authorizationstatus.md)
  Returns a value indicating whether the app is authorized to retrieve stored motion data.
- [enum CMAuthorizationStatus](cmauthorizationstatus.md)
  The authorization status for motion-related features.
### Starting and Stopping Activity Updates
- [func startActivityUpdates(to: OperationQueue, withHandler: CMMotionActivityHandler)](cmmotionactivitymanager/startactivityupdates(to:withhandler:).md)
  Starts the delivery of current motion data updates to your app.
- [func stopActivityUpdates()](cmmotionactivitymanager/stopactivityupdates.md)
  Stops the delivery of motion updates to your app
- [typealias CMMotionActivityHandler](cmmotionactivityhandler.md)
  A block that reports the current motion associated with the device.
### Getting Historical Activity Data
- [func queryActivityStarting(from: Date, to: Date, to: OperationQueue, withHandler: CMMotionActivityQueryHandler)](cmmotionactivitymanager/queryactivitystarting(from:to:to:withhandler:).md)
  Gathers and returns historical motion data for the specified time period
- [typealias CMMotionActivityQueryHandler](cmmotionactivityqueryhandler.md)
  A block that reports the motion updates that occurred between the specified query interval.

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

- [class CMHeadphoneActivityManager](cmheadphoneactivitymanager.md)
  An object that starts and manages headphone activity services.
- [class CMMotionActivity](cmmotionactivity.md)
  The data for a single motion update event.
- [Getting motion-activity data from headphones](getting-motion-activity-data-from-headphones.md)
  Configure your app to listen for motion-activity changes from headphones.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager)*