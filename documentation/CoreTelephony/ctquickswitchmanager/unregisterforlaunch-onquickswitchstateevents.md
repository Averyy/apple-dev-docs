# unregisterForLaunch(onQuickSwitchStateEvents:)

**Framework**: Core Telephony  
**Kind**: method

Removes the calling app’s registration for background launch on quick switch state changes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
func unregisterForLaunchOnQuickSwitchStateEvents() async throws
```

#### Discussion

Call this method when you want to de-register the current device so it no longer receives quick switch event notifications when your app isn’t running.

After this call succeeds, the system no longer launches the app  in the background when the device’s QuickSwitch state transitions. The framework calls the completion handler with a non-`nil` error if the app was not previously registered or if the the framework couldn’t complete the request.

## Parameters

- `completionHandler`: A completion handler the framework calls after processing the request. The parameter passed to the completion handler indicates whether the request succeeded, failed, or ended in an unknown state.

## See Also

- [func registerForLaunch(onQuickSwitchStateEvents: ((any Error)?) -> Void)](ctquickswitchmanager/registerforlaunch(onquickswitchstateevents:).md)
  Registers the calling app for background launch whenever the device’s quick switch state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctquickswitchmanager/unregisterforlaunch(onquickswitchstateevents:))*