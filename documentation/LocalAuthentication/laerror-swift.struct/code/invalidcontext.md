# LAError.Code.invalidContext

**Framework**: Local Authentication  
**Kind**: case  
**Role**: Case

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

```c
LAErrorInvalidContext
```

#### Discussion

You invalidate a context by calling its [`invalidate()`](../../lacontext/invalidate%28%29.md) method.

## See Also

### Other errors
- [LAError.Code.authenticationFailed](./authenticationfailed.md)
  The user failed to provide valid credentials.
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

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laerror-swift.struct/code/invalidcontext)*