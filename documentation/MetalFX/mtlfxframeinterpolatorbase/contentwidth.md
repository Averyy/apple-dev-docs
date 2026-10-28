# contentWidth

**Framework**: MetalFX  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The width, in pixels, of the content region within the input textures to process.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.1+

## Declaration

```swift
var contentWidth: Int { get set }
```

```objc
@property (nonatomic, readwrite) NSUInteger contentWidth;
```

## Discussion

Use this property together with [`contentHeight`](./contentheight.md) to specify a subrectangle of the input textures for the frame interpolator to process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase/contentwidth)*