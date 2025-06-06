# mtkView(_:drawableSizeWillChange:)

**Framework**: MetalKit  
**Kind**: method  
**Required**: Yes

Updates the view’s contents upon receiving a change in layout, resolution, or size.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func mtkView(_ view: MTKView, drawableSizeWillChange size: CGSize)
```

#### Discussion

Use this method to recompute any view or projection matrices, or to regenerate any buffers to be compatible with the view’s new size.

## Parameters

- `view`: The view requesting that its contents be updated.
- `size`: The view’s new drawable size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkviewdelegate/mtkview(_:drawablesizewillchange:))*