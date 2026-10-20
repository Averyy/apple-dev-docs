# LAError.Code.authenticationFailed

**Framework**: Local Authentication  
**Kind**: case  
**Role**: Case

The user failed to provide valid credentials.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case authenticationFailed
```

```c
LAErrorAuthenticationFailed
```

## See Also

### Other errors
- [LAError.Code.invalidContext](./invalidcontext.md)
  The context was previously invalidated.
- [LAError.Code.invalidDimensions](./invaliddimensions.md)
- [LAError.Code.notInteractive](./notinteractive.md)
  Displaying the required authentication user interface is forbidden.
- [LAError.Code.passcodeNotSet](./passcodenotset.md)
  A passcode isn’t set on the device.
- [LAError.Code.userFallback](./userfallback.md)
  The user tapped the fallback button in the authentication dialog, but no fallback is available for the authentication policy.
- [LAError.Code.watchNotAvailable](./watchnotavailable.md)
  An attempt to authenticate with Apple Watch failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laerror-swift.struct/code/authenticationfailed)*