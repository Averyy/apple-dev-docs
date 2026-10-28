# LAError.Code.watchNotAvailable

**Framework**: Local Authentication  
**Kind**: case  
**Role**: Case

An attempt to authenticate with Apple Watch failed.

**Availability**:
- macOS 10.15+ - Deprecated in 15.0 (renamed: LAError.companionNotAvailable)

## Declaration

```swift
case watchNotAvailable
```

```c
LAErrorWatchNotAvailable
```

## Discussion

You receive this error when the system fails to locate a nearby, paired Apple Watch running watchOS 6 or later while trying to authenticate using one of the watch authentication policies like [`deviceOwnerAuthenticationWithWatch`](../../lapolicy/deviceownerauthenticationwithwatch.md).

## See Also

### Other errors
- [LAError.Code.authenticationFailed](./authenticationfailed.md)
  The user failed to provide valid credentials.
- [LAError.Code.invalidContext](./invalidcontext.md)
  The context was previously invalidated.
- [LAError.Code.invalidDimensions](./invaliddimensions.md)
- [LAError.Code.notInteractive](./notinteractive.md)
  Displaying the required authentication user interface is forbidden.
- [LAError.Code.passcodeNotSet](./passcodenotset.md)
  A passcode isn’t set on the device.
- [LAError.Code.userFallback](./userfallback.md)
  The user tapped the fallback button in the authentication dialog, but no fallback is available for the authentication policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laerror-swift.struct/code/watchnotavailable)*