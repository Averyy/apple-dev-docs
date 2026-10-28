# path(in:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Describes this shape as a path within a rectangular frame of reference.

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
nonisolated
func path(in rect: CGRect) -> Path
```

## Return Value

A path that describes this shape.

## Parameters

- `rect`: The frame of reference for describing this shape.

## See Also

### Defining a shape’s size and path
- [func sizeThatFits(ProposedViewSize) -> CGSize](./sizethatfits%28_%29.md)
  Returns the size of the view that will render the shape, given a proposed size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/path(in:))*