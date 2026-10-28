# offset(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Changes the relative position of this shape using the specified size.

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
func offset(_ offset: CGSize) -> OffsetShape<Self>
```

**Other overloads**:

```swift
nonisolated
func offset(_ offset: CGPoint) -> OffsetShape<Self>
```

## Return Value

A shape offset by the specified amount.

## Discussion

The following example renders two circles. It places one circle at its default position. The second circle is outlined with a stroke, positioned on top of the first circle and offset by 100 points to the left and 50 points below.

```swift
Circle()
.overlay(
    Circle()
    .offset(CGSize(width: -100, height: 50))
    .stroke()
)
```

## Parameters

- `offset`: The amount, in points, by which you offset the shape. Negative numbers are to the left and up; positive numbers are to the right and down.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/offset(_:)-8jkk1)*