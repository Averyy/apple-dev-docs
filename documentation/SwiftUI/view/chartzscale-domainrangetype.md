# chartZScale(domain:range:type:)

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
func chartZScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType? = nil) -> some View where Domain : ScaleDomain, Range : PositionScaleRange
```

## Parameters

- `domain`: The possible data values along the z axis in the   chart. You can define the domain with a   for numeric values.
- `range`: The range of x positions that correspond to the scale   domain. By default the range is determined by the dimension of the plot   area.
- `type`: The scale type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartzscale(domain:range:type:))*