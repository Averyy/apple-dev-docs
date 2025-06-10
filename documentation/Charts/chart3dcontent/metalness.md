# metalness(_:)

**Framework**: Swift Charts  
**Kind**: method

A value that controls whether the surface has a metallic look.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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