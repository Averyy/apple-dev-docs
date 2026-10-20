# PTInstantiationError.Code.missingEntitlement

**Framework**: Push to Talk  
**Kind**: case  
**Role**: Case

An instantiation error that indicates the app is missing the entitlement.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
case missingEntitlement
```

```c
PTInstantiationErrorMissingEntitlement
```

## See Also

### Error codes
- [PTInstantiationError.Code.unknown](./unknown.md)
  An instantiation error that indicates an unknown error.
- [PTInstantiationError.Code.invalidPlatform](./invalidplatform.md)
  An instantiation error that indicates the API isn’t available on the simulator or macOS devices.
- [PTInstantiationError.Code.missingBackgroundMode](./missingbackgroundmode.md)
  An instantiation error that indicates the app doesn’t have the background mode in an enabled state.
- [PTInstantiationError.Code.missingPushServerEnvironment](./missingpushserverenvironment.md)
  An instantiation error that indicates the app doesn’t have the push notification capability in an enabled state.
- [PTInstantiationError.Code.instantiationAlreadyInProgress](./instantiationalreadyinprogress.md)
  An instantiation error that indicates there’s already an in-flight instantiation request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptinstantiationerror-swift.struct/code/missingentitlement)*