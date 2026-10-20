# getDeviceState(_:)

**Framework**: Core Telephony  
**Kind**: method  
**Role**: Instance Method

Gets the quick switch state of the current device.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
func getDeviceState(_ completionHandler: @escaping @Sendable (CTQuickSwitchState, (any Error)?) -> Void)
```

```swift
var deviceState: CTQuickSwitchState { get async throws }
```

```objc
- (void) getDeviceState:(void (^)(CTQuickSwitchState state, NSError *error)) completionHandler;
```

## Parameters

- `completionHandler`: A completion handler the framework calls after processing the request. The parameters passed to the completion handler indicate the [`CTQuickSwitchState`](../ctquickswitchstate.md) and an error value that indicates whether the request succeeded, failed, or ended in an unknown state.

## See Also

### Checking the state of a device
- [func getPhoneNumberState(forSuffix: String, completion: (CTQuickSwitchState, (any Error)?) -> Void)](./getphonenumberstate%28forsuffix,completion%29.md)
  Queries the quick switch state for a phone number whose suffix matches the provided phone number suffix.
- [enum CTQuickSwitchState](../ctquickswitchstate.md)
  Values that describe a device’s quick switch status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctquickswitchmanager/getdevicestate(_:))*