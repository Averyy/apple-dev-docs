# aspectRatio

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The ratio between width and height of the screen.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var aspectRatio: Float { get set }
```

#### Discussion

In a 3D game, you set this value to the same aspect ratio you use to create your perspective matrix, which is typically `width/height`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase/aspectratio)*