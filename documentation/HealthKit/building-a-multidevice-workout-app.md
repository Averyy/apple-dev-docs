# Building a multidevice workout app

**Framework**: HealthKit

Mirror a workout from a watchOS app to its companion iOS app, and perform bidirectional communication between them.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- watchOS 10.0+
- Xcode 15.0+

#### Overview

> **Note**: This sample code project is associated with WWDC23 session 10023: [`Build a multidevice workout app`](https://developer.apple.comhttps://developer.apple.com/wwdc23/10023/).

##### Configure the Sample Code Project

This sample code project needs to run on physical devices. Before you run it with Xcode:

- Set the developer team for all targets to let Xcode automatically manage the provisioning profile. For more information, see [`Assign a project to a team`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev23aab79b4).
- In the Info pane of the `MirroringWorkoutsSample Watch App` target, change the value of the `WKCompanionAppBundleIdentifier` key to the bundle ID of the iOS app.

## See Also

- [Running workout sessions](running-workout-sessions.md)
  Track a workout on Apple Watch.
- [Build a workout app for Apple Watch](build-a-workout-app-for-apple-watch.md)
  Create your own workout app, quickly and easily, with HealthKit and SwiftUI.
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/building-a-multidevice-workout-app)*