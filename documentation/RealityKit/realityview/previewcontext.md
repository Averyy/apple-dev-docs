# previewContext(_:)

**Framework**: RealityKit  
**Kind**: method

Declares a context for the preview.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func previewContext<C>(_ value: C) -> some View where C : PreviewContext
```

## Parameters

- `value`: The context for the preview; the default is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/previewcontext(_:))*