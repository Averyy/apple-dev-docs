# Build a workout app for Apple Watch

**Framework**: HealthKit

Create your own workout app, quickly and easily, with HealthKit and SwiftUI.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- watchOS 8.0+
- Xcode 14.2+

#### Overview

> **Note**: This sample code project is associated with WWDC21 session [`10009: Build a workout app for Apple Watch`](https://developer.apple.comhttps://developer.apple.com/wwdc21/10009/).

##### Configure the Sample Code Project

Before you run the sample code project in Xcode:

1. Open the sample with the latest version of Xcode.
2. Select the top-level project.
3. For the three targets, select the correct team in the Signing & Capabilities pane (next to Team) to let Xcode automatically manage your provisioning profile.
4. Make a note of the Bundle Identifier of the WatchKit App target.
5. Open the `Info.plist` file of the WatchKit Extension target, and change the value of the `NSExtension` > `NSExtensionAttributes` > `WKAppBundleIdentifier` key to the bundle ID you noted in the previous step.
6. Make a clean build and run the sample app on your device.

## See Also

- [Running workout sessions](running-workout-sessions.md)
  Track a workout on Apple Watch.
- [Building a multidevice workout app](building-a-multidevice-workout-app.md)
  Mirror a workout from a watchOS app to its companion iOS app, and perform bidirectional communication between them.
- [Building a workout app for iPhone and iPad](building-a-workout-app-for-iphone-and-ipad.md)
  Start a workout in iOS, control it from the Lock Screen with App Intents, and present the workout status with Live Activities.
- [class HKWorkoutSession](hkworkoutsession.md)
  A session that tracks the user’s workout on Apple Watch.
- [class HKWorkoutConfiguration](hkworkoutconfiguration.md)
  An object that contains configuration information about a workout session.
- [enum HKWorkoutSessionState](hkworkoutsessionstate.md)
  A workout session’s state.
- [class HKLiveWorkoutBuilder](hkliveworkoutbuilder.md)
  A builder object that constructs a workout incrementally based on live data from an active workout session.
- [class HKLiveWorkoutDataSource](hkliveworkoutdatasource.md)
  A data source that automatically provides live data from an active workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/build-a-workout-app-for-apple-watch)*