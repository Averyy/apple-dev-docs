# buttonBorderShape(_:)

**Framework**: RealityKit  
**Kind**: method

Sets the border shape for buttons in this view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func buttonBorderShape(_ shape: ButtonBorderShape) -> some View
```

#### Discussion

The border shape is used to draw the platter for a bordered button. In macOS, some border shapes are only applicable to bordered buttons in widgets.

The border shape affects buttons of the `PrimitiveButtonStyle/bordered` and `PrimitiveButtonStyle/borderedProminent` styles.

## Parameters

- `shape`: The shape to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3d/buttonbordershape(_:))*