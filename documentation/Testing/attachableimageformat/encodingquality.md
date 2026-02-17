# encodingQuality

**Framework**: Swift Testing  
**Kind**: property

The encoding quality to use for this image format.

**Availability**:
- Swift 6.3+
- Xcode 26.4+ (Beta)

## Declaration

```swift
var encodingQuality: Float { get }
```

#### Discussion

The meaning of the value is format-specific with `0.0` being the lowest supported encoding quality and `1.0` being the highest supported encoding quality. The value of this property is ignored for image formats that do not support variable encoding quality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachableimageformat/encodingquality)*