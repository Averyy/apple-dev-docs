# instantiationAlreadyInProgress

**Framework**: Push to Talk  
**Kind**: property  
**Role**: Type Property

An instantiation error that indicates there’s already an in-flight instantiation request.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
static var instantiationAlreadyInProgress: PTInstantiationError.Code { get }
```

## See Also

### Constants
- [static var unknown: PTInstantiationError.Code](./unknown.md)
  An instantiation error that indicates an unknown error.
- [static var invalidPlatform: PTInstantiationError.Code](./invalidplatform.md)
  An instantiation error that indicates the API isn’t available on the simulator or macOS devices.
- [static var missingBackgroundMode: PTInstantiationError.Code](./missingbackgroundmode.md)
  An instantiation error that indicates the app doesn’t have the background mode in an enabled state.
- [static var missingPushServerEnvironment: PTInstantiationError.Code](./missingpushserverenvironment.md)
  An instantiation error that indicates the app doesn’t have the push notification capability in an enabled state.
- [static var missingEntitlement: PTInstantiationError.Code](./missingentitlement.md)
  An instantiation error that indicates the app is missing the entitlement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptinstantiationerror-swift.struct/instantiationalreadyinprogress)*