# Getting motion-activity data from headphones

**Framework**: Core Motion

Configure your app to listen for motion-activity changes from headphones.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Xcode 16.1+

#### Overview

This sample app demonstrates how to use `CMHeadphoneActivityManager` to request updates when the current type of motion changes. When a change occurs, the app receives update information as a [`CMMotionActivity`](CMMotionActivity.md) object, which it uses to show a text description of the motion change.

##### Configure the Sample Code Project

Because this sample app uses headphone motion updates, it needs to run on a device, not in Simulator.  To run this sample, you’ll need the following:

- An iOS device with iOS 18 or later
- Headphones that support motion updates, such as AirPods Pro 2 or AirPods 4

## See Also

- [class CMMotionActivityManager](cmmotionactivitymanager.md)
  An object that manages access to the motion data stored by the device.
- [class CMHeadphoneActivityManager](cmheadphoneactivitymanager.md)
  An object that starts and manages headphone activity services.
- [class CMMotionActivity](cmmotionactivity.md)
  The data for a single motion update event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/getting-motion-activity-data-from-headphones)*