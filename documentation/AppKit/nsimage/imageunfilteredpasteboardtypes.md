# imageUnfilteredPasteboardTypes()

**Framework**: AppKit  
**Kind**: method

Returns an array of strings identifying the pasteboard types supported directly by the registered image representation objects.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class func imageUnfilteredPasteboardTypes() -> [NSPasteboard.PasteboardType]
```

#### Return Value

An array of `NSString` objects, each of which identifies a single supported pasteboard type.

#### Discussion

The returned list does not contain pasteboard types that are supported only through a user-installed filter service.

## See Also

- [class func imageFileTypes() -> [String]](nsimage/imagefiletypes.md)
  Returns an array of strings identifying the image types supported by the registered image representation objects.
- [class func imageUnfilteredFileTypes() -> [String]](nsimage/imageunfilteredfiletypes.md)
  Returns an array of strings identifying the file types supported directly by the registered image representation objects.
- [class func imagePasteboardTypes() -> [NSPasteboard.PasteboardType]](nsimage/imagepasteboardtypes.md)
  Returns an array of strings identifying the pasteboard types supported directly by the registered image representation objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/imageunfilteredpasteboardtypes())*