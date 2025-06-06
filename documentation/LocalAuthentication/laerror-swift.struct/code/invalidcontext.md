# LAError.Code.invalidContext

**Framework**: Local Authentication  
**Kind**: case

The context was previously invalidated.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case invalidContext
```

#### Discussion

You invalidate a context by calling its [`invalidate()`](lacontext/invalidate().md) method.

## See Also

- [LAError.Code.authenticationFailed](laerror-swift.struct/code/authenticationfailed.md)
  The user failed to provide valid credentials.
- [LAError.Code.invalidDimensions](laerror-swift.struct/code/invaliddimensions.md)
- [LAError.Code.notInteractive](laerror-swift.struct/code/notinteractive.md)
  Displaying the required authentication user interface is forbidden.
- [LAError.Code.passcodeNotSet](laerror-swift.struct/code/passcodenotset.md)
  A passcode isn’t set on the device.
- [LAError.Code.userFallback](laerror-swift.struct/code/userfallback.md)
  The user tapped the fallback button in the authentication dialog, but no fallback is available for the authentication policy.
- [LAError.Code.watchNotAvailable](laerror-swift.struct/code/watchnotavailable.md)
  An attempt to authenticate with Apple Watch failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laerror-swift.struct/code/invalidcontext)*