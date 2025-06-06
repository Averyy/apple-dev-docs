# inverse

**Framework**: SwiftUI  
**Kind**: property

An option to invert the shape or layer alpha as the clip mask.

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
static var inverse: GraphicsContext.ClipOptions { get }
```

#### Discussion

When you use this option, SwiftUI uses `1 - alpha` instead of `alpha` for the given clip shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/clipoptions/inverse)*