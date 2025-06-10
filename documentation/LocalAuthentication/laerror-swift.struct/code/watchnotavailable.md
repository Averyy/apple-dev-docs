# LAError.Code.watchNotAvailable

**Framework**: Local Authentication  
**Kind**: case

An attempt to authenticate with Apple Watch failed.

**Availability**:
- macOS 10.15+

## Declaration

```swift
case watchNotAvailable
```

#### Discussion

You receive this error when the system fails to locate a nearby, paired Apple Watch running watchOS 6 or later while trying to authenticate using one of the watch authentication policies like [`deviceOwnerAuthenticationWithWatch`](lapolicy/deviceownerauthenticationwithwatch.md).

## See Also

- [LAError.Code.authenticationFailed](laerror-swift.struct/code/authenticationfailed.md)
  The user failed to provide valid credentials.
- [LAError.Code.invalidContext](laerror-swift.struct/code/invalidcontext.md)
  The context was previously invalidated.
- [LAError.Code.invalidDimensions](laerror-swift.struct/code/invaliddimensions.md)
- [LAError.Code.notInteractive](laerror-swift.struct/code/notinteractive.md)
  Displaying the required authentication user interface is forbidden.
- [LAError.Code.passcodeNotSet](laerror-swift.struct/code/passcodenotset.md)
  A passcode isn’t set on the device.
- [LAError.Code.userFallback](laerror-swift.struct/code/userfallback.md)
  The user tapped the fallback button in the authentication dialog, but no fallback is available for the authentication policy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laerror-swift.struct/code/watchnotavailable)*