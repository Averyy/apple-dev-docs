# CMMotionActivity

**Framework**: Core Motion  
**Kind**: class

The data for a single motion update event.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 15.0+
- watchOS 2.0+

## Declaration

```swift
class CMMotionActivity
```

#### Overview

On devices that support motion, you can use a [`CMMotionActivityManager`](cmmotionactivitymanager.md) or [`CMHeadphoneActivityManager`](cmheadphoneactivitymanager.md) object to request updates when the current type of motion changes. When a change occurs, the update information is packaged into a [`CMMotionActivity`](cmmotionactivity.md) object and sent to your app.

The motion-related properties of this class aren’t mutually exclusive. In other words, it’s possible for more than one of the motion-related properties to contain the value [`true`](https://developer.apple.com/documentation/swift/true). For example, if the user was driving in a car and the car stopped at a red light, the update event associated with that change in motion would have both the [`automotive`](cmmotionactivity/automotive.md) and [`stationary`](cmmotionactivity/stationary.md) properties set to [`true`](https://developer.apple.com/documentation/swift/true). It’s also possible for all of the properties to be set to [`false`](https://developer.apple.com/documentation/swift/false) when the device is in motion but the movement doesn’t correlate to walking, running, cycling, or automotive travel.

You don’t create instances of this class yourself. The [`CMMotionActivityManager`](cmmotionactivitymanager.md) object creates them and sends them to the handler block you registered. For more information about how to initiate the delivery of motion activity updates to your app, see [`CMMotionActivityManager`](cmmotionactivitymanager.md).

## Topics

### Getting the Type of Motion
- [var stationary: Bool](cmmotionactivity/stationary.md)
  A Boolean indicating whether the device is stationary.
- [var walking: Bool](cmmotionactivity/walking.md)
  A Boolean indicating whether the device is on a walking person.
- [var running: Bool](cmmotionactivity/running.md)
  A Boolean indicating whether the device is on a running person.
- [var automotive: Bool](cmmotionactivity/automotive.md)
  A Boolean indicating whether the device is in an automobile.
- [var cycling: Bool](cmmotionactivity/cycling.md)
  A Boolean indicating whether the device is in a bicycle.
- [var unknown: Bool](cmmotionactivity/unknown.md)
  A Boolean indicating whether the type of motion is unknown.
### Getting Metadata for the Motion
- [var startDate: Date](cmmotionactivity/startdate.md)
  The time at which the change in motion occurred.
- [var confidence: CMMotionActivityConfidence](cmmotionactivity/confidence.md)
  The confidence in the assessment of the motion type.
- [enum CMMotionActivityConfidence](cmmotionactivityconfidence.md)
  The confidence that the motion data is accurate.

## Relationships

### Inherits From
- [CMLogItem](cmlogitem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CMMotionActivityManager](cmmotionactivitymanager.md)
  An object that manages access to the motion data stored by the device.
- [class CMHeadphoneActivityManager](cmheadphoneactivitymanager.md)
  An object that starts and manages headphone activity services.
- [Getting motion-activity data from headphones](getting-motion-activity-data-from-headphones.md)
  Configure your app to listen for motion-activity changes from headphones.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionactivity)*