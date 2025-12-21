# rect(corners:isUniform:)

**Framework**: SwiftUI  
**Kind**: method

A rectangle shape that is aligned inside the frame of the view containing it. The same corner style will be set on four corners to be square, rounded, or concentric to the container shape.

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
static func rect(corners: Edge.Corner.Style, isUniform: Bool = false) -> Self
```

## Parameters

- `corners`: The corner style for all four corners.
- `isUniform`: Should the corner style on each corner be applied   individually or uniformly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/rect(corners:isuniform:))*