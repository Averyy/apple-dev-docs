# contentDescription

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An alternate textual description of the image contents.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var contentDescription: String { get }
```

```objc
@property (copy, readonly) NSString * contentDescription;
```

#### Discussion

This string contains a brief description of the image, which is useful for searches or places where you need a text-based description. The adaptive image derives the content of this property from the underlying image data.

## See Also

### Getting the content metadata
- [var contentIdentifier: String](./contentidentifier.md)
  A unique identifier for this image.
- [class var contentType: UTType](./contenttype.md)
  The image data format to use for this image type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsadaptiveimageglyph/contentdescription)*