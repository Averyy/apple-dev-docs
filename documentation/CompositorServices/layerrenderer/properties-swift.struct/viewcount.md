# viewCount

**Framework**: Compositor Services  
**Kind**: property

The number of views that you must fill with content.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
var viewCount: Int { get }
```

#### Discussion

This property tells you how many views you’re responsible for filling with your content. For example, this function returns `1` for a monoscopic display and `2` for a stereoscopic display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/properties-swift.struct/viewcount)*