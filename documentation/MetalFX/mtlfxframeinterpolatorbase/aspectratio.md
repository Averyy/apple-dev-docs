# aspectRatio

**Framework**: MetalFX  
**Kind**: property  
**Required**: Yes

The ratio between width and height of the screen.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var aspectRatio: Float { get set }
```

#### Discussion

In a 3D game, you set this value to the same aspect ratio you use to create your perspective matrix, which is typically `width/height`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatorbase/aspectratio)*