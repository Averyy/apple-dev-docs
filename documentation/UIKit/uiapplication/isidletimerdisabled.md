# isIdleTimerDisabled

**Framework**: UIKit  
**Kind**: property

A Boolean value that controls whether the idle timer is disabled for the app.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isIdleTimerDisabled: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false). When most apps have no touches as user input for a short period, the system puts the device into a “sleep” state where the screen dims. This is done for the purposes of conserving power. However, apps that don’t have user input except for the accelerometer — games, for instance — can, by setting this property to [`true`](https://developer.apple.com/documentation/swift/true), disable the “idle timer” to avert system sleep.

> ❗ **Important**:  You should set this property only if necessary and should be sure to reset it to [`false`](https://developer.apple.com/documentation/swift/false) when the need no longer exists. Most apps should let the system turn off the screen when the idle timer elapses. This includes audio apps. With appropriate use of Audio Session Services, playback and recording proceed uninterrupted when the screen turns off. The only apps that should disable the idle timer are mapping apps, games, or programs where the app needs to continue displaying content when user interaction is minimal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/isidletimerdisabled)*