# AAError

**Framework**: Accessory Access  
**Kind**: struct

Values that describe errors the AccessoryAccess framework returns.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
struct AAError
```

## Topics

### Errors
- [static var accessoryListenerAlreadyRegistered: AAError.Code](aaerror/accessorylisteneralreadyregistered.md)
  An error that indicates the accessory listener is already registered, and therefore the app can’t re-register it.
- [static var accessoryNotAccessible: AAError.Code](aaerror/accessorynotaccessible.md)
  An error that indicates the USB accessory isn’t accessible.
- [static var internalError: AAError.Code](aaerror/internalerror.md)
  An error that represents an internal error.
- [static var invalidAccessoryState: AAError.Code](aaerror/invalidaccessorystate.md)
  An error that indicates the accessory isn’t in the correct state for the current operation.
- [AAError.Code](aaerror/code.md)
  Values that represent error codes that the AccessoryAccess framework returns.
### Type properties
- [static var errorDomain: String](aaerror/errordomain.md)
  A value that represents the Accessory Access framework’s error domain.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let AAErrorDomain: String](aaerrordomain.md)
  The string that represents the framework’s error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aaerror)*