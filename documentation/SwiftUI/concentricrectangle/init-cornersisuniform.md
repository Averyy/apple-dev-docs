# init(corners:isUniform:)

**Framework**: SwiftUI  
**Kind**: init

Create a rectangle with the same corner style set on four corners.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(corners: Edge.Corner.Style, isUniform: Bool = false)
```

#### Discussion

A [`ConcentricRectangle`](concentricrectangle.md) with all four corners set to concentric individually can vary in resolved radius. This can happen when the rectangle is not centered within the container shape, or the container shape itself has different radius per corner. If set to be uniform, [`ConcentricRectangle`](concentricrectangle.md) will resolve each corner on its own first, then pick the largest resolved radius out of the corners and apply it uniformly to achieve the symmetric look.

## Parameters

- `corners`: The corner style for all four corners.
- `isUniform`: Should the corner style on each corner be applied   individually or uniformly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/concentricrectangle/init(corners:isuniform:))*