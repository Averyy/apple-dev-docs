# subscript(_:)

**Framework**: Metal  
**Kind**: subscript

Maps a physical color attachment index to a logical index.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
subscript(logicalIndex: Int) -> Int { get set }
```

#### Overview

To set the physical index, which represents the render pass color attachment index `P`, for a logical index, which represents the pipeline state’s configuration for a color attachment `L`, assign: `myMapping[L] = P`. To retrieve a stored physical index use `let P = myMapping[L]`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllogicaltophysicalcolorattachmentmap/subscript(_:))*