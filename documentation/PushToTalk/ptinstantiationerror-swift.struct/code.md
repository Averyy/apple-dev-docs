# PTInstantiationError.Code

**Framework**: Push to Talk  
**Kind**: enum

Error codes for instantiation operations.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
enum Code
```

## Topics

### Error codes
- [PTInstantiationError.Code.unknown](ptinstantiationerror-swift.struct/code/unknown.md)
  An instantiation error that indicates an unknown error.
- [PTInstantiationError.Code.invalidPlatform](ptinstantiationerror-swift.struct/code/invalidplatform.md)
  An instantiation error that indicates the API isn’t available on the simulator or macOS devices.
- [PTInstantiationError.Code.missingBackgroundMode](ptinstantiationerror-swift.struct/code/missingbackgroundmode.md)
  An instantiation error that indicates the app doesn’t have the background mode in an enabled state.
- [PTInstantiationError.Code.missingPushServerEnvironment](ptinstantiationerror-swift.struct/code/missingpushserverenvironment.md)
  An instantiation error that indicates the app doesn’t have the push notification capability in an enabled state.
- [PTInstantiationError.Code.missingEntitlement](ptinstantiationerror-swift.struct/code/missingentitlement.md)
  An instantiation error that indicates the app is missing the entitlement.
- [PTInstantiationError.Code.instantiationAlreadyInProgress](ptinstantiationerror-swift.struct/code/instantiationalreadyinprogress.md)
  An instantiation error that indicates there’s already an in-flight instantiation request.
### Initializers
- [init?(rawValue: Int)](ptinstantiationerror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct PTChannelError](ptchannelerror-swift.struct.md)
  A structure that represents a channel error.
- [PTChannelError.Code](ptchannelerror-swift.struct/code.md)
  Error codes for channel operations.
- [struct PTInstantiationError](ptinstantiationerror-swift.struct.md)
  A structure that represents an instantiation error.
- [let PTChannelErrorDomain: String](ptchannelerrordomain.md)
  A string representation of the channel error domain.
- [let PTInstantiationErrorDomain: String](ptinstantiationerrordomain.md)
  A string representation of the instantiation error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptinstantiationerror-swift.struct/code)*