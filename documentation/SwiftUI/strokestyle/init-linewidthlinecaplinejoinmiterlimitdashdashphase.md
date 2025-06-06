# init(lineWidth:lineCap:lineJoin:miterLimit:dash:dashPhase:)

**Framework**: SwiftUI  
**Kind**: init

Creates a new stroke style from the given components.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(lineWidth: CGFloat = 1, lineCap: CGLineCap = .butt, lineJoin: CGLineJoin = .miter, miterLimit: CGFloat = 10, dash: [CGFloat] = [CGFloat](), dashPhase: CGFloat = 0)
```

## Parameters

- `lineWidth`: The width of the segment.
- `lineCap`: The endpoint style of a segment.
- `lineJoin`: The join type of a segment.
- `miterLimit`: The threshold used to determine whether to use a bevel   instead of a miter at a join.
- `dash`: The lengths of painted and unpainted segments used to make a   dashed line.
- `dashPhase`: How far into the dash pattern the line starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/strokestyle/init(linewidth:linecap:linejoin:miterlimit:dash:dashphase:))*