# registerForLaunch(onQuickSwitchStateEvents:)

**Framework**: Core Telephony  
**Kind**: method  
**Role**: Type Method

Registers the calling app for background launch whenever the device’s quick switch state changes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
class func registerForLaunch(onQuickSwitchStateEvents completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
class func registerForLaunchOnQuickSwitchStateEvents() async throws
```

```objc
+ (void) registerForLaunchOnQuickSwitchStateEvents:(void (^)(NSError *error)) completionHandler;
```

## Discussion

> ❗ **Important**: This only applies to apps that someone has set to be the default messaging or default calling app. For more information on becoming the default messaging app, see [Preparing your app to be the default messaging app](../../Messages/preparing-your-app-to-be-the-default-messaging-app.md). For more info on becoming the default calling app, see [Preparing your app to be the default calling app](../../CallKit/preparing-your-app-to-be-the-default-calling-app.md).

Call this method when you want to register the current device to receive quick switch event notifications when your app isn’t running.

If an app successfully registers to receive these events, the system allocates runtime to the app to process state changes even if it’s not currently running at the time of a stage change.

Registration persists until the app explicitly removes itself with [`unregisterForLaunch(onQuickSwitchStateEvents:)`](./unregisterforlaunch%28onquickswitchstateevents%29.md).

The framework calls the completion handler with a non-`nil` error if the app is not eligible to register.

## Parameters

- `completionHandler`: A completion handler the framework calls after processing the request. The parameter passed to the completion handler indicates whether the request succeeded, failed, or ended in an unknown state.

## See Also

### Registering and unregistering for quick switch events
- [class func unregisterForLaunch(onQuickSwitchStateEvents: ((any Error)?) -> Void)](./unregisterforlaunch%28onquickswitchstateevents%29.md)
  Removes the calling app’s registration for background launch on quick switch state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctquickswitchmanager/registerforlaunch(onquickswitchstateevents:))*