# init(headroom:colorSpace:colorComponents:locations:count:)

**Framework**: Core Graphics  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init?(headroom: Float, colorSpace space: CGColorSpace, colorComponents components: UnsafePointer<CGFloat>, locations: UnsafePointer<CGFloat>?, count: Int)
```

```c
extern CGGradientRefCGGradientCreateWithContentHeadroom(float headroom, CGColorSpaceRef space, const CGFloat *components, const CGFloat *locations, size_t count);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cggradient/init(headroom:colorspace:colorcomponents:locations:count:))*