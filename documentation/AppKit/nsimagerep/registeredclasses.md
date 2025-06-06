# registeredClasses

**Framework**: AppKit  
**Kind**: property

Returns an array containing the registered image representation classes.

**Availability**:
- macOS ?+

## Declaration

```swift
class var registeredClasses: [AnyClass] { get }
```

#### Return Value

An array of `Class` objects identifying the registered `NSImageRep` subclasses.

## See Also

- [class func `class`(forType: String) -> AnyClass?](nsimagerep/class(fortype:).md)
  Returns the image representation subclass that handles image data for the specified UTI.
- [class func `class`(for: Data) -> AnyClass?](nsimagerep/class(for:).md)
  Returns the image representation subclass that handles the specified type of data.
- [class func registerClass(AnyClass)](nsimagerep/registerclass(_:).md)
  Adds the specified class to the registry of available image representation subclasses.
- [class func unregisterClass(AnyClass)](nsimagerep/unregisterclass(_:).md)
  Removes the specified image representation subclass from the registry of available image representations.
- [class func `class`(forFileType: String) -> AnyClass?](nsimagerep/class(forfiletype:).md)
  Returns the image representation subclass that handles data with the specified type.
- [class func `class`(forPasteboardType: NSPasteboard.PasteboardType) -> AnyClass?](nsimagerep/class(forpasteboardtype:).md)
  Returns the image representation subclass that handles data with the specified pasteboard type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/registeredclasses)*