# opacity

**Framework**: SwiftUI  
**Kind**: property

The opacity of drawing operations in the context.

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
var opacity: Double { get set }
```

#### Discussion

Set this value to affect the opacity of content that you subsequently draw into the context. Changing this value has no impact on the content you previously drew into the context.

## See Also

- [var blendMode: GraphicsContext.BlendMode](graphicscontext/blendmode-swift.property.md)
  The blend mode used by drawing operations in the context.
- [GraphicsContext.BlendMode](graphicscontext/blendmode-swift.struct.md)
  The ways that a graphics context combines new content with background content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/opacity)*