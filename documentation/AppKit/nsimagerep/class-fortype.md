# class(forType:)

**Framework**: AppKit  
**Kind**: method

Returns the image representation subclass that handles image data for the specified UTI.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class func `class`(forType type: String) -> AnyClass?
```

#### Return Value

A `Class` object for the image representation that can handle the UTI, or `nil` if no image representation could handle the data.

## Parameters

- `type`: The UTI string identifying the desired image type. Some sample image-related UTI strings include “ ”, “ ”, and “ ”. For a list of supported types, see  .

## See Also

- [class func `class`(for: Data) -> AnyClass?](nsimagerep/class(for:).md)
  Returns the image representation subclass that handles the specified type of data.
- [class var registeredClasses: [AnyClass]](nsimagerep/registeredclasses.md)
  Returns an array containing the registered image representation classes.
- [class func registerClass(AnyClass)](nsimagerep/registerclass(_:).md)
  Adds the specified class to the registry of available image representation subclasses.
- [class func unregisterClass(AnyClass)](nsimagerep/unregisterclass(_:).md)
  Removes the specified image representation subclass from the registry of available image representations.
- [class func `class`(forFileType: String) -> AnyClass?](nsimagerep/class(forfiletype:).md)
  Returns the image representation subclass that handles data with the specified type.
- [class func `class`(forPasteboardType: NSPasteboard.PasteboardType) -> AnyClass?](nsimagerep/class(forpasteboardtype:).md)
  Returns the image representation subclass that handles data with the specified pasteboard type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/class(fortype:))*