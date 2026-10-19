# class(forPasteboardType:)

**Framework**: AppKit  
**Kind**: method

Returns the image representation subclass that handles data with the specified pasteboard type.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class func `class`(forPasteboardType type: NSPasteboard.PasteboardType) -> AnyClass?
```

#### Return Value

A `Class` object for the image representation that can handle the specified pasteboard type, or `nil` if no image representation could handle the type.

## Parameters

- `type`: The pasteboard type.

## See Also

- [class func imageFileTypes() -> [String]](nsimagerep/imagefiletypes.md)
  Returns the file types supported by the image representation class or one of its subclasses.
- [class func imagePasteboardTypes() -> [NSPasteboard.PasteboardType]](nsimagerep/imagepasteboardtypes.md)
  Returns the pasteboard types supported by the image representation class or one of its subclasses.
- [class func imageUnfilteredFileTypes() -> [String]](nsimagerep/imageunfilteredfiletypes.md)
  Returns the list of file types supported directly by the image representation.
- [class func imageUnfilteredPasteboardTypes() -> [NSPasteboard.PasteboardType]](nsimagerep/imageunfilteredpasteboardtypes.md)
  Returns the list of pasteboard types supported directly by the image representation.
- [class func `class`(forFileType: String) -> AnyClass?](nsimagerep/class(forfiletype:).md)
  Returns the image representation subclass that handles data with the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/class(forpasteboardtype:))*