# init(centered:anchor:multiLabelAlignment:collisionResolution:offsetsMarks:orientation:horizontalSpacing:verticalSpacing:)

**Framework**: Swift Charts  
**Kind**: init

Constructs axis value labels with the given properties and default text.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
init(centered: Bool? = nil, anchor: UnitPoint? = nil, multiLabelAlignment: Alignment? = nil, collisionResolution: AxisValueLabelCollisionResolution = .automatic, offsetsMarks: Bool? = nil, orientation: AxisValueLabelOrientation = .automatic, horizontalSpacing: CGFloat? = nil, verticalSpacing: CGFloat? = nil) where Content == Never
```

## Parameters

- `centered`: Whether to center the label between two axis values.   If  , default to true for discrete data, false to continuous data.
- `anchor`: The anchor point on the bounding box of the text element that attaches to the  .
- `multiLabelAlignment`: How labels along the axis are aligned with each other.
- `collisionResolution`: How labels that collide with others are resolved.
- `offsetsMarks`: Whether to offset marks to accomodate for the space used by the label.
- `orientation`: The orientation of the label.
- `horizontalSpacing`: The horizontal spacing of the label.   If  , a default spacing will be used.
- `verticalSpacing`: The vertical spacing of the label.   If  , a default spacing will be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/axisvaluelabel/init(centered:anchor:multilabelalignment:collisionresolution:offsetsmarks:orientation:horizontalspacing:verticalspacing:))*