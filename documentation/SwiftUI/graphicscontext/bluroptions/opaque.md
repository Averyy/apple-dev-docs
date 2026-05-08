# opaque

**Framework**: SwiftUI  
**Kind**: property

An option that causes the filter to ensure the result is completely opaque.

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
static var opaque: GraphicsContext.BlurOptions { get }
```

#### Discussion

The filter ensure opacity by dividing each pixel by its alpha value. The result may be undefined if the input to the filter isn’t also completely opaque.

## See Also

- [static var dithersResult: GraphicsContext.BlurOptions](graphicscontext/bluroptions/dithersresult.md)
  An option that causes the filter to dither the result, to reduce banding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/bluroptions/opaque)*