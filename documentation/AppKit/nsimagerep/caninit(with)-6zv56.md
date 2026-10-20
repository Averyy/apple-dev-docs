# canInit(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the image representation can initialize itself from the specified data.

**Availability**:
- macOS

## Declaration

```swift
class func canInit(with data: Data) -> Bool
```

```objc
+ (BOOL) canInitWithData:(NSData *) data;
```

#### Return Value

[`true`](../../Swift/true.md) if the receiver understands the format of the specified data and can use it to initialize itself; otherwise, [`false`](../../Swift/false.md).

#### Discussion

This method should be overridden by subclasses. Note that this method does not need to do a comprehensive check of the image data; it should return [`false`](../../Swift/false.md) only if it knows it cannot initialize itself from the data.

## Parameters

- `data`: The image data.

## See Also

### Determining Types for Images
- [class func canInit(with: NSPasteboard) -> Bool](./caninit%28with%29-56pum.md)
  Returns a Boolean value that indicates whether the receiver can initialize itself from the data on the specified pasteboard.
- [class var imageTypes: [String]](./imagetypes.md)
  Returns an array of UTI strings identifying the image types supported by the image representation, either directly or through a user-installed filter service.
- [class var imageUnfilteredTypes: [String]](./imageunfilteredtypes.md)
  Returns an array of UTI strings identifying the image types supported directly by the ime representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/caninit(with:)-6zv56)*