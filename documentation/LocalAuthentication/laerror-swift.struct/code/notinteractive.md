# LAError.Code.notInteractive

**Framework**: Local Authentication  
**Kind**: case

Displaying the required authentication user interface is forbidden.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case notInteractive
```

#### Discussion

Permit the display of the authentication UI by setting the [`interactionNotAllowed`](lacontext/interactionnotallowed.md) property to [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [LAError.Code.authenticationFailed](laerror-swift.struct/code/authenticationfailed.md)
  The user failed to provide valid credentials.
- [LAError.Code.invalidContext](laerror-swift.struct/code/invalidcontext.md)
  The context was previously invalidated.
- [LAError.Code.invalidDimensions](laerror-swift.struct/code/invaliddimensions.md)
- [LAError.Code.passcodeNotSet](laerror-swift.struct/code/passcodenotset.md)
  A passcode isn’t set on the device.
- [LAError.Code.userFallback](laerror-swift.struct/code/userfallback.md)
  The user tapped the fallback button in the authentication dialog, but no fallback is available for the authentication policy.
- [LAError.Code.watchNotAvailable](laerror-swift.struct/code/watchnotavailable.md)
  An attempt to authenticate with Apple Watch failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laerror-swift.struct/code/notinteractive)*