# getDeviceState(_:)

**Framework**: Core Telephony  
**Kind**: method

Gets the quick switch state of the current device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
var deviceState: CTQuickSwitchState { get async throws }
```

## Parameters

- `completionHandler`: A completion handler the framework calls after processing the request. The parameters passed to the completion handler indicate the [`CTQuickSwitchState`](ctquickswitchstate.md) and an error value that indicates whether the request succeeded, failed, or ended in an unknown state.

## See Also

- [func getPhoneNumberState(forSuffix: String, completion: (CTQuickSwitchState, (any Error)?) -> Void)](ctquickswitchmanager/getphonenumberstate(forsuffix:completion:).md)
  Queries the quick switch state for a phone number whose suffix matches the provided phone number suffix.
- [enum CTQuickSwitchState](ctquickswitchstate.md)
  Values that describe a device’s quick switch status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctquickswitchmanager/getdevicestate(_:))*