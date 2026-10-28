# contentIdentifier

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A unique identifier for this image.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var contentIdentifier: String { get }
```

```objc
@property (readonly) NSString * contentIdentifier;
```

## Discussion

Use this property to create a persistent reference to this specific image in your code. The image data contains this content identifier, so the value persists between instantiations.

## See Also

### Getting the content metadata
- [var contentDescription: String](./contentdescription.md)
  An alternate textual description of the image contents.
- [class var contentType: UTType](./contenttype.md)
  The image data format to use for this image type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsadaptiveimageglyph/contentidentifier)*