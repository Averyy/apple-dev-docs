# class(for:)

**Framework**: AppKit  
**Kind**: method

Returns the image representation subclass that handles the specified type of data.

**Availability**:
- macOS ?+

## Declaration

```swift
class func `class`(for data: Data) -> AnyClass?
```

#### Return Value

A `Class` object for the image representation that can handle the data, or `nil` if no image representation could handle the data.

## Parameters

- `data`: The image data.

## See Also

- [class func `class`(forType: String) -> AnyClass?](nsimagerep/class(fortype:).md)
  Returns the image representation subclass that handles image data for the specified UTI.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/class(for:))*