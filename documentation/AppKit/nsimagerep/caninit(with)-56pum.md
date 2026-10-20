# canInit(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the receiver can initialize itself from the data on the specified pasteboard.

**Availability**:
- macOS

## Declaration

```swift
class func canInit(with pasteboard: NSPasteboard) -> Bool
```

```objc
+ (BOOL) canInitWithPasteboard:(NSPasteboard *) pasteboard;
```

#### Return Value

[`true`](../../Swift/true.md) if the receiver understands the format of the specified data and can use it to initialize itself; otherwise, [`false`](../../Swift/false.md).

#### Discussion

This method invokes the [`imageUnfilteredPasteboardTypes()`](./imageunfilteredpasteboardtypes%28%29.md) class method and checks the list of types returned by that method against the data types in `pasteboard`. If it finds a match, it returns [`true`](../../Swift/true.md). When creating a subclass of `NSImageRep` that accepts image data from a non-default pasteboard type, override the [`imageUnfilteredPasteboardTypes()`](./imageunfilteredpasteboardtypes%28%29.md) method to assure this method returns the correct response.

## Parameters

- `pasteboard`: The pasteboard containing the image data.

## See Also

### Determining Types for Images
- [class func canInit(with: Data) -> Bool](./caninit%28with%29-6zv56.md)
  Returns a Boolean value that indicates whether the image representation can initialize itself from the specified data.
- [class var imageTypes: [String]](./imagetypes.md)
  Returns an array of UTI strings identifying the image types supported by the image representation, either directly or through a user-installed filter service.
- [class var imageUnfilteredTypes: [String]](./imageunfilteredtypes.md)
  Returns an array of UTI strings identifying the image types supported directly by the ime representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/caninit(with:)-56pum)*