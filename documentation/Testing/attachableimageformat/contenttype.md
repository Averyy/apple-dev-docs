# contentType

**Framework**: Swift Testing  
**Kind**: property

The content type corresponding to this image format.

**Availability**:
- Swift 6.3+
- Xcode 26.4+ (Beta)

## Declaration

```swift
var contentType: UTType { get }
```

#### Discussion

For example, if this image format equals [`png`](attachableimageformat/png.md), the value of this property equals [`UTType.png`](https://developer.apple.comhttps://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/png).

The value of this property always conforms to [`UTType.image`](https://developer.apple.comhttps://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/image).


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachableimageformat/contenttype)*