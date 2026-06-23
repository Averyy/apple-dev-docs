# registerForLaunch(onQuickSwitchStateEvents:)

**Framework**: Core Telephony  
**Kind**: method

Registers the calling app for background launch whenever the device’s quick switch state changes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
class func registerForLaunchOnQuickSwitchStateEvents() async throws
```

#### Discussion

> ❗ **Important**: This only applies to apps that someone has set to be the default messaging or default calling app. For more information on becoming the default messaging app, see [`Preparing your app to be the default messaging app`](https://developer.apple.com/documentation/Messages/Preparing-your-app-to-be-the-default-messaging-app). For more info on becoming the default calling app, see [`Preparing your app to be the default calling app`](https://developer.apple.com/documentation/CallKit/Preparing-your-app-to-be-the-default-calling-app).

Call this method when you want to register the current device to receive quick switch event notifications when your app isn’t running.

If an app successfully registers to receive these events, the system allocates runtime to the app to process state changes even if it’s not currently running at the time of a stage change.

Registration persists until the app explicitly removes itself with [`unregisterForLaunch(onQuickSwitchStateEvents:)`](ctquickswitchmanager/unregisterforlaunch(onquickswitchstateevents:).md).

The framework calls the completion handler with a non-`nil` error if the app is not eligible to register.

## Parameters

- `completionHandler`: A completion handler the framework calls after processing the request. The parameter passed to the completion handler indicates whether the request succeeded, failed, or ended in an unknown state.

## See Also

- [class func unregisterForLaunch(onQuickSwitchStateEvents: ((any Error)?) -> Void)](ctquickswitchmanager/unregisterforlaunch(onquickswitchstateevents:).md)
  Removes the calling app’s registration for background launch on quick switch state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctquickswitchmanager/registerforlaunch(onquickswitchstateevents:))*