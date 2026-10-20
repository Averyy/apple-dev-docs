# NEAppPushManagerError.Code

**Framework**: Network Extension  
**Kind**: enum  
**Role**: Enumeration

Error codes that the local push API declares.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

```c
enum NEAppPushManagerError : NSInteger;
```

## Topics

### Error codes
- [NEAppPushManagerError.Code.configurationInvalid](./code/configurationinvalid.md)
  An error code that indicates the app push configuration is invalid.
- [NEAppPushManagerError.Code.configurationNotLoaded](./code/configurationnotloaded.md)
  An error code that indicates the manager hasn’t loaded the app push configuration.
- [NEAppPushManagerError.Code.inactiveSession](./code/inactivesession.md)
  An error code that indicates an invalid attempt to perform an operation on an inactive session.
- [NEAppPushManagerError.Code.internalError](./code/internalerror.md)
  An error code that indicates an internal error in the local push connectivity framework.
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

### Handling errors
- [struct NEAppPushManagerError](../neapppushmanagererror-swift.struct.md)
  An error that the push manager encounters.
- [let NEAppPushErrorDomain: String](../neapppusherrordomain.md)
  The error domain string for local push errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushmanagererror-swift.struct/code)*