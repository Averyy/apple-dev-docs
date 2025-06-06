# invalidPlatform

**Framework**: Push to Talk  
**Kind**: property

An instantiation error that indicates the API isn’t available on the simulator or macOS devices.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
static var invalidPlatform: PTInstantiationError.Code { get }
```

## See Also

- [static var unknown: PTInstantiationError.Code](ptinstantiationerror-swift.struct/unknown.md)
  An instantiation error that indicates an unknown error.
- [static var missingBackgroundMode: PTInstantiationError.Code](ptinstantiationerror-swift.struct/missingbackgroundmode.md)
  An instantiation error that indicates the app doesn’t have the background mode in an enabled state.
- [static var missingPushServerEnvironment: PTInstantiationError.Code](ptinstantiationerror-swift.struct/missingpushserverenvironment.md)
  An instantiation error that indicates the app doesn’t have the push notification capability in an enabled state.
- [static var missingEntitlement: PTInstantiationError.Code](ptinstantiationerror-swift.struct/missingentitlement.md)
  An instantiation error that indicates the app is missing the entitlement.
- [static var instantiationAlreadyInProgress: PTInstantiationError.Code](ptinstantiationerror-swift.struct/instantiationalreadyinprogress.md)
  An instantiation error that indicates there’s already an in-flight instantiation request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptinstantiationerror-swift.struct/invalidplatform)*