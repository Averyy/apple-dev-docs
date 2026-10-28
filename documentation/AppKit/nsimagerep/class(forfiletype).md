# class(forFileType:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the image representation subclass that handles data with the specified type.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use [`class(forType:)`](./class%28fortype%29.md) instead.

## Declaration

```swift
class func `class`(forFileType type: String) -> AnyClass?
```

```objc
+ (Class) imageRepClassForFileType:(NSString *) type;
```

## Return Value

A `Class` object for the image representation that can handle the type of data, or `nil` if no image representation could handle the type.

## Parameters

- `type`: A string containing the filename extension or an encoded HFS type.

## See Also

### Deprecated methods
- [class func imageFileTypes() -> [String]](./imagefiletypes%28%29.md)
  Returns the file types supported by the image representation class or one of its subclasses.
- [class func imagePasteboardTypes() -> [NSPasteboard.PasteboardType]](./imagepasteboardtypes%28%29.md)
  Returns the pasteboard types supported by the image representation class or one of its subclasses.
- [class func imageUnfilteredFileTypes() -> [String]](./imageunfilteredfiletypes%28%29.md)
  Returns the list of file types supported directly by the image representation.
- [class func imageUnfilteredPasteboardTypes() -> [NSPasteboard.PasteboardType]](./imageunfilteredpasteboardtypes%28%29.md)
  Returns the list of pasteboard types supported directly by the image representation.
- [class func `class`(forPasteboardType: NSPasteboard.PasteboardType) -> AnyClass?](./class%28forpasteboardtype%29.md)
  Returns the image representation subclass that handles data with the specified pasteboard type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/class(forfiletype:))*