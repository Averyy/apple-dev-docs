# AAError.Code

**Framework**: Accessory Access  
**Kind**: enum

Values that represent error codes that the AccessoryAccess framework returns.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
enum Code
```

#### Overview

The AccessoryAccess framework can also report errors from other domains when the error originates from a lower level component. The `NSError` domain for the AccessoryAccess framework is `AAErrorDomain`, the code is one of the `AAErrorCode` constants.

## Topics

### Error codes
- [AAError.Code.accessoryListenerAlreadyRegistered](aaerror/code/accessorylisteneralreadyregistered.md)
  An error code that indicates there’s already an accessory listener for the USB accessory.
- [AAError.Code.accessoryNotAccessible](aaerror/code/accessorynotaccessible.md)
  An error code that indicates the USB accessory isn’t accessible since it may already be in use.
- [AAError.Code.internalError](aaerror/code/internalerror.md)
  An error value that represents an internal error.
- [AAError.Code.invalidAccessoryState](aaerror/code/invalidaccessorystate.md)
  An error value that indicates the accessory isn’t in the correct state for the current operation.
### Creating an error code
- [init?(rawValue: Int)](aaerror/code/init(rawvalue:).md)
  Creates a new error code with the provided value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static var accessoryListenerAlreadyRegistered: AAError.Code](aaerror/accessorylisteneralreadyregistered.md)
  An error that indicates the accessory listener is already registered, and therefore the app can’t re-register it.
- [static var accessoryNotAccessible: AAError.Code](aaerror/accessorynotaccessible.md)
  An error that indicates the USB accessory isn’t accessible.
- [static var internalError: AAError.Code](aaerror/internalerror.md)
  An error that represents an internal error.
- [static var invalidAccessoryState: AAError.Code](aaerror/invalidaccessorystate.md)
  An error that indicates the accessory isn’t in the correct state for the current operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aaerror/code)*