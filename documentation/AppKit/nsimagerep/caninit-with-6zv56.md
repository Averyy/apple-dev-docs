# canInit(with:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether the image representation can initialize itself from the specified data.

**Availability**:
- macOS ?+

## Declaration

```swift
class func canInit(with data: Data) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver understands the format of the specified data and can use it to initialize itself; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method should be overridden by subclasses. Note that this method does not need to do a comprehensive check of the image data; it should return [`false`](https://developer.apple.com/documentation/Swift/false) only if it knows it cannot initialize itself from the data.

## Parameters

- `data`: The image data.

## See Also

- [class func canInit(with: NSPasteboard) -> Bool](nsimagerep/caninit(with:)-56pum.md)
  Returns a Boolean value that indicates whether the receiver can initialize itself from the data on the specified pasteboard.
- [class var imageTypes: [String]](nsimagerep/imagetypes.md)
  Returns an array of UTI strings identifying the image types supported by the image representation, either directly or through a user-installed filter service.
- [class var imageUnfilteredTypes: [String]](nsimagerep/imageunfilteredtypes.md)
  Returns an array of UTI strings identifying the image types supported directly by the ime representation.
- [class func imageFileTypes() -> [String]](nsimagerep/imagefiletypes.md)
  Returns the file types supported by the image representation class or one of its subclasses.
- [class func imagePasteboardTypes() -> [NSPasteboard.PasteboardType]](nsimagerep/imagepasteboardtypes.md)
  Returns the pasteboard types supported by the image representation class or one of its subclasses.
- [class func imageUnfilteredFileTypes() -> [String]](nsimagerep/imageunfilteredfiletypes.md)
  Returns the list of file types supported directly by the image representation.
- [class func imageUnfilteredPasteboardTypes() -> [NSPasteboard.PasteboardType]](nsimagerep/imageunfilteredpasteboardtypes.md)
  Returns the list of pasteboard types supported directly by the image representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/caninit(with:)-6zv56)*