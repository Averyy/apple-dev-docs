# metalness(_:)

**Framework**: Swift Charts  
**Kind**: method

A value that controls whether the surface has a metallic look.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
func metalness(_ ratio: Double) -> some Chart3DContent
```

#### Discussion

Zero represents a non-metallic (dielectric) surface. One represents a metallic surface. In real life, materials are either metallic or dielectric (0 or 1).

## Parameters

- `ratio`: The degree of metalness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chart3dcontent/metalness(_:))*