# annotation(position:alignment:spacing:overflowResolution:content:)

**Framework**: Swift Charts  
**Kind**: method

Annotates this mark or collection of marks with a view positioned relative to its bounds.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func annotation<C>(position: AnnotationPosition = .automatic, alignment: Alignment = .center, spacing: CGFloat? = nil, overflowResolution: AnnotationOverflowResolution, @ViewBuilder content: @escaping (AnnotationContext) -> C) -> some ChartContent where C : View
```

## Parameters

- `position`: The location relative to the item being annotated at which   the annotation will be placed.
- `alignment`: The guide for aligning the annotation in the specified position.
- `spacing`: Distance between the annotation and the annotated content,   or   if you want to use the default distance.
- `overflowResolution`: How to resolve the annotation exceeding the boundary of the plot.
- `content`: A view builder that creates the annotation.

## See Also

- [func annotation<C>(position: AnnotationPosition, alignment: Alignment, spacing: CGFloat?, content: () -> C) -> some ChartContent](chartcontent/annotation(position:alignment:spacing:content:)-65emh.md)
  Annotates this mark or collection of marks with a view positioned relative to its bounds.
- [func annotation<C>(position: AnnotationPosition, alignment: Alignment, spacing: CGFloat?, content: (AnnotationContext) -> C) -> some ChartContent](chartcontent/annotation(position:alignment:spacing:content:)-26b2f.md)
  Annotates this mark or collection of marks with a view positioned relative to its bounds.
- [func annotation<C>(position: AnnotationPosition, alignment: Alignment, spacing: CGFloat?, overflowResolution: AnnotationOverflowResolution, content: () -> C) -> some ChartContent](chartcontent/annotation(position:alignment:spacing:overflowresolution:content:)-1kiow.md)
  Annotates this mark or collection of marks with a view positioned relative to its bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent/annotation(position:alignment:spacing:overflowresolution:content:)-6w4p3)*