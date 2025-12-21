# canInit(with:)

**Framework**: AppKit  
**Kind**: method

Tests whether the image can create an instance of itself using pasteboard data.

**Availability**:
- macOS ?+

## Declaration

```swift
class func canInit(with pasteboard: NSPasteboard) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver knows how to handle the data on the pasteboard; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method uses the `NSImageRep` class method [`imageUnfilteredPasteboardTypes()`](nsimagerep/imageunfilteredpasteboardtypes().md) to find a class that can handle the data in the specified pasteboard. If you create your own `NSImageRep` subclasses, override the [`imageUnfilteredPasteboardTypes()`](nsimagerep/imageunfilteredpasteboardtypes().md) method to notify `NSImage` of the pasteboard types your class supports.

## Parameters

- `pasteboard`: The pasteboard containing the image data.

## See Also

- [class func imagePasteboardTypes() -> [NSPasteboard.PasteboardType]](nsimage/imagepasteboardtypes.md)
  Returns an array of strings identifying the pasteboard types supported directly by the registered image representation objects.
- [class var imageTypes: [String]](nsimage/imagetypes.md)
  Returns an array of UTI strings identifying the image types supported by the registered image representation objects, either directly or through a user-installed filter service.
- [class var imageUnfilteredTypes: [String]](nsimage/imageunfilteredtypes.md)
  Returns an array of UTI strings identifying the image types supported directly by the registered image representation objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/caninit(with:))*