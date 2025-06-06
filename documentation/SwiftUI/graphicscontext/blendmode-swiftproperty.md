# blendMode

**Framework**: SwiftUI  
**Kind**: property

The blend mode used by drawing operations in the context.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var blendMode: GraphicsContext.BlendMode { get set }
```

#### Discussion

Set this value to affect how any content that you subsequently draw into the context blends with content that’s already in the context. Use one of the [`GraphicsContext.BlendMode`](graphicscontext/blendmode-swift.struct.md) values.

## See Also

- [var opacity: Double](graphicscontext/opacity.md)
  The opacity of drawing operations in the context.
- [GraphicsContext.BlendMode](graphicscontext/blendmode-swift.struct.md)
  The ways that a graphics context combines new content with background content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/blendmode-swift.property)*