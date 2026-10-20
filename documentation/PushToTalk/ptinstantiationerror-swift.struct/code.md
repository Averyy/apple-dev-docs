# PTInstantiationError.Code

**Framework**: Push to Talk  
**Kind**: enum  
**Role**: Enumeration

Error codes for instantiation operations.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
enum Code
```

```c
enum PTInstantiationError : NSInteger;
```

## Topics

### Error codes
- [PTInstantiationError.Code.unknown](./code/unknown.md)
  An instantiation error that indicates an unknown error.
- [PTInstantiationError.Code.invalidPlatform](./code/invalidplatform.md)
  An instantiation error that indicates the API isn’t available on the simulator or macOS devices.
- [PTInstantiationError.Code.missingBackgroundMode](./code/missingbackgroundmode.md)
  An instantiation error that indicates the app doesn’t have the background mode in an enabled state.
- [PTInstantiationError.Code.missingPushServerEnvironment](./code/missingpushserverenvironment.md)
  An instantiation error that indicates the app doesn’t have the push notification capability in an enabled state.
- [PTInstantiationError.Code.missingEntitlement](./code/missingentitlement.md)
  An instantiation error that indicates the app is missing the entitlement.
- [PTInstantiationError.Code.instantiationAlreadyInProgress](./code/instantiationalreadyinprogress.md)
  An instantiation error that indicates there’s already an in-flight instantiation request.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Push to Talk errors
- [struct PTChannelError](../ptchannelerror-swift.struct.md)
  A structure that represents a channel error.
- [PTChannelError.Code](../ptchannelerror-swift.struct/code.md)
  Error codes for channel operations.
- [struct PTInstantiationError](../ptinstantiationerror-swift.struct.md)
  A structure that represents an instantiation error.
- [let PTChannelErrorDomain: String](../ptchannelerrordomain.md)
  A string representation of the channel error domain.
- [let PTInstantiationErrorDomain: String](../ptinstantiationerrordomain.md)
  A string representation of the instantiation error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptinstantiationerror-swift.struct/code)*