# contentType

**Framework**: Swift Testing  
**Kind**: property  
**Role**: Instance Property

The content type corresponding to this image format.

**Availability**:
- Swift 6.3+
- Xcode 26.4+

## Declaration

```swift
var contentType: UTType { get }
```

#### Discussion

For example, if this image format equals [`png`](./png.md), the value of this property equals [UTType.png](../../UniformTypeIdentifiers/uttype-swift.struct/png.md).

The value of this property always conforms to [UTType.image](../../UniformTypeIdentifiers/uttype-swift.struct/image.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachableimageformat/contenttype)*