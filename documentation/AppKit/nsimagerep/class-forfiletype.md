# class(forFileType:)

**Framework**: AppKit  
**Kind**: method

Returns the image representation subclass that handles data with the specified type.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class func `class`(forFileType type: String) -> AnyClass?
```

#### Return Value

A `Class` object for the image representation that can handle the type of data, or `nil` if no image representation could handle the type.

## Parameters

- `type`: A string containing the filename extension or an encoded HFS type.

## See Also

- [class func `class`(forType: String) -> AnyClass?](nsimagerep/class(fortype:).md)
  Returns the image representation subclass that handles image data for the specified UTI.
- [class func `class`(for: Data) -> AnyClass?](nsimagerep/class(for:).md)
  Returns the image representation subclass that handles the specified type of data.
- [class var registeredClasses: [AnyClass]](nsimagerep/registeredclasses.md)
  Returns an array containing the registered image representation classes.
- [class func registerClass(AnyClass)](nsimagerep/registerclass(_:).md)
  Adds the specified class to the registry of available image representation subclasses.
- [class func unregisterClass(AnyClass)](nsimagerep/unregisterclass(_:).md)
  Removes the specified image representation subclass from the registry of available image representations.
- [class func `class`(forPasteboardType: NSPasteboard.PasteboardType) -> AnyClass?](nsimagerep/class(forpasteboardtype:).md)
  Returns the image representation subclass that handles data with the specified pasteboard type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/class(forfiletype:))*