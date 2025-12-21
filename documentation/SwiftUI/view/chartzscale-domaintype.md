# chartZScale(domain:type:)

**Framework**: SwiftUI  
**Kind**: method

Configures the z scale for 3D charts.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
func chartZScale<Domain>(domain: Domain, type: ScaleType? = nil) -> some View where Domain : ScaleDomain
```

## Parameters

- `domain`: The possible data values along the z axis in the   chart. You can define the domain with a   for numeric values (e.g.,  ).
- `type`: The scale type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartzscale(domain:type:))*