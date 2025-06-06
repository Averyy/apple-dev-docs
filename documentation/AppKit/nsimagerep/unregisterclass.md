# unregisterClass(_:)

**Framework**: AppKit  
**Kind**: method

Removes the specified image representation subclass from the registry of available image representations.

**Availability**:
- macOS ?+

## Declaration

```swift
class func unregisterClass(_ imageRepClass: AnyClass)
```

#### Discussion

This method posts the [`registryDidChangeNotification`](nsimagerep/registrydidchangenotification.md), along with the receiving object, to the default notification center.

## Parameters

- `imageRepClass`: The   object for an   subclass.

## See Also

- [class func `class`(forType: String) -> AnyClass?](nsimagerep/class(fortype:).md)
  Returns the image representation subclass that handles image data for the specified UTI.
- [class func `class`(for: Data) -> AnyClass?](nsimagerep/class(for:).md)
  Returns the image representation subclass that handles the specified type of data.
- [class var registeredClasses: [AnyClass]](nsimagerep/registeredclasses.md)
  Returns an array containing the registered image representation classes.
- [class func registerClass(AnyClass)](nsimagerep/registerclass(_:).md)
  Adds the specified class to the registry of available image representation subclasses.
- [class func `class`(forFileType: String) -> AnyClass?](nsimagerep/class(forfiletype:).md)
  Returns the image representation subclass that handles data with the specified type.
- [class func `class`(forPasteboardType: NSPasteboard.PasteboardType) -> AnyClass?](nsimagerep/class(forpasteboardtype:).md)
  Returns the image representation subclass that handles data with the specified pasteboard type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/unregisterclass(_:))*