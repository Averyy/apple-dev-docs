# accessoryNotAccessible

**Framework**: Accessory Access  
**Kind**: property

An error that indicates the USB accessory isn’t accessible.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
static var accessoryNotAccessible: AAError.Code { get }
```

## See Also

- [static var accessoryListenerAlreadyRegistered: AAError.Code](aaerror/accessorylisteneralreadyregistered.md)
  An error that indicates the accessory listener is already registered, and therefore the app can’t re-register it.
- [static var internalError: AAError.Code](aaerror/internalerror.md)
  An error that represents an internal error.
- [static var invalidAccessoryState: AAError.Code](aaerror/invalidaccessorystate.md)
  An error that indicates the accessory isn’t in the correct state for the current operation.
- [AAError.Code](aaerror/code.md)
  Values that represent error codes that the AccessoryAccess framework returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryaccess/aaerror/accessorynotaccessible)*