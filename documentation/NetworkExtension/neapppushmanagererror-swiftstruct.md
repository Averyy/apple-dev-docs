# NEAppPushManagerError

**Framework**: Network Extension  
**Kind**: struct

An error that the push manager encounters.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
struct NEAppPushManagerError
```

## Topics

### Inspecting error properties
- [NEAppPushManagerError.Code](neapppushmanagererror-swift.struct/code.md)
  Error codes that the local push API declares.
### Error constants
- [static var configurationInvalid: NEAppPushManagerError.Code](neapppushmanagererror-swift.struct/configurationinvalid.md)
  An error that indicates the app push configuration is invalid.
- [static var configurationNotLoaded: NEAppPushManagerError.Code](neapppushmanagererror-swift.struct/configurationnotloaded.md)
  An error that indicates the manager hasn’t loaded the app push configuration.
- [static var inactiveSession: NEAppPushManagerError.Code](neapppushmanagererror-swift.struct/inactivesession.md)
  An error that indicates an invalid attempt to perform an operation on an inactive session.
- [static var internalError: NEAppPushManagerError.Code](neapppushmanagererror-swift.struct/internalerror.md)
  An error that indicates an internal error in the local push connectivity framework.
### Type Properties
- [static var errorDomain: String](neapppushmanagererror-swift.struct/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let NEAppPushErrorDomain: String](neapppusherrordomain.md)
  The error domain string for local push errors.
- [NEAppPushManagerError.Code](neapppushmanagererror-swift.struct/code.md)
  Error codes that the local push API declares.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushmanagererror-swift.struct)*