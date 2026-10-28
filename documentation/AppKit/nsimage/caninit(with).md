# canInit(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Tests whether the image can create an instance of itself using pasteboard data.

**Availability**:
- macOS

## Declaration

```swift
class func canInit(with pasteboard: NSPasteboard) -> Bool
```

```objc
+ (BOOL) canInitWithPasteboard:(NSPasteboard *) pasteboard;
```

## Return Value

[`true`](../../Swift/true.md) if the receiver knows how to handle the data on the pasteboard; otherwise, [`false`](../../Swift/false.md).

## Discussion

This method uses the `NSImageRep` class method [`imageUnfilteredPasteboardTypes()`](../nsimagerep/imageunfilteredpasteboardtypes%28%29.md) to find a class that can handle the data in the specified pasteboard. If you create your own `NSImageRep` subclasses, override the [`imageUnfilteredPasteboardTypes()`](../nsimagerep/imageunfilteredpasteboardtypes%28%29.md) method to notify `NSImage` of the pasteboard types your class supports.

## Parameters

- `pasteboard`: The pasteboard containing the image data.

## See Also

### Related Documentation
- [class func imagePasteboardTypes() -> [NSPasteboard.PasteboardType]](./imagepasteboardtypes%28%29.md)
  Returns an array of strings identifying the pasteboard types supported directly by the registered image representation objects.
### Determining Supported Types of Images
- [class var imageTypes: [String]](./imagetypes.md)
  Returns an array of UTI strings identifying the image types supported by the registered image representation objects, either directly or through a user-installed filter service.
- [class var imageUnfilteredTypes: [String]](./imageunfilteredtypes.md)
  Returns an array of UTI strings identifying the image types supported directly by the registered image representation objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/caninit(with:))*