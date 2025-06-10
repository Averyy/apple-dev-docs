# NEAppPushManagerError.Code

**Framework**: Network Extension  
**Kind**: enum

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

## Topics

### Error codes
- [NEAppPushManagerError.Code.configurationInvalid](neapppushmanagererror-swift.struct/code/configurationinvalid.md)
  An error code that indicates the app push configuration is invalid.
- [NEAppPushManagerError.Code.configurationNotLoaded](neapppushmanagererror-swift.struct/code/configurationnotloaded.md)
  An error code that indicates the manager hasn’t loaded the app push configuration.
- [NEAppPushManagerError.Code.inactiveSession](neapppushmanagererror-swift.struct/code/inactivesession.md)
  An error code that indicates an invalid attempt to perform an operation on an inactive session.
- [NEAppPushManagerError.Code.internalError](neapppushmanagererror-swift.struct/code/internalerror.md)
  An error code that indicates an internal error in the local push connectivity framework.
### Initializers
- [init?(rawValue: Int)](neapppushmanagererror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct NEAppPushManagerError](neapppushmanagererror-swift.struct.md)
  An error that the push manager encounters.
- [let NEAppPushErrorDomain: String](neapppusherrordomain.md)
  The error domain string for local push errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushmanagererror-swift.struct/code)*