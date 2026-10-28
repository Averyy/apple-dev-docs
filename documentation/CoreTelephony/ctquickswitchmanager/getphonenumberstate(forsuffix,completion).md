# getPhoneNumberState(forSuffix:completion:)

**Framework**: Core Telephony  
**Kind**: method  
**Role**: Instance Method

Queries the quick switch state for a phone number whose suffix matches the provided phone number suffix.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
func getPhoneNumberState(forSuffix phoneNumberSuffix: String, completion completionHandler: @escaping @Sendable (CTQuickSwitchState, (any Error)?) -> Void)
```

```swift
func phoneNumberState(forSuffix phoneNumberSuffix: String) async throws -> CTQuickSwitchState
```

```objc
- (void) getPhoneNumberStateForSuffix:(NSString *) phoneNumberSuffix completion:(void (^)(CTQuickSwitchState state, NSError *error)) completionHandler;
```

## Discussion

- Parameters

  - phoneNumberSuffix: The last 4 digits of the phone number to check. The framework presents a person with a consent screen to provide this information to the requesting app. If a person denies consent, the app returns [`CTQuickSwitchState.notEnrolled`](../ctquickswitchstate/notenrolled.md) and no error value.
  - completionHandler: A completion handler the framework calls after processing the request. The parameters the framework passes to the completion handler indicate the [`CTQuickSwitchState`](../ctquickswitchstate.md) and an error value that indicates whether the request succeeded, failed, or ended in an unknown state.

## Discussion

The framework presents a person with a consent screen to provide this information to the requesting app. If someone denies consent, the app returns [`CTQuickSwitchState.notEnrolled`](../ctquickswitchstate/notenrolled.md) and no error.

## See Also

### Checking the state of a device
- [func getDeviceState((CTQuickSwitchState, (any Error)?) -> Void)](./getdevicestate%28_%29.md)
  Gets the quick switch state of the current device.
- [enum CTQuickSwitchState](../ctquickswitchstate.md)
  Values that describe a device’s quick switch status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctquickswitchmanager/getphonenumberstate(forsuffix:completion:))*