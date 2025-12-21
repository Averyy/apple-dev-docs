# canInit(with:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether the receiver can initialize itself from the data on the specified pasteboard.

**Availability**:
- macOS ?+

## Declaration

```swift
class func canInit(with pasteboard: NSPasteboard) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver understands the format of the specified data and can use it to initialize itself; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method invokes the [`imageUnfilteredPasteboardTypes()`](nsimagerep/imageunfilteredpasteboardtypes().md) class method and checks the list of types returned by that method against the data types in `pasteboard`. If it finds a match, it returns [`true`](https://developer.apple.com/documentation/Swift/true). When creating a subclass of `NSImageRep` that accepts image data from a non-default pasteboard type, override the [`imageUnfilteredPasteboardTypes()`](nsimagerep/imageunfilteredpasteboardtypes().md) method to assure this method returns the correct response.

## Parameters

- `pasteboard`: The pasteboard containing the image data.

## See Also

- [class func canInit(with: Data) -> Bool](nsimagerep/caninit(with:)-6zv56.md)
  Returns a Boolean value that indicates whether the image representation can initialize itself from the specified data.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/caninit(with:)-56pum)*