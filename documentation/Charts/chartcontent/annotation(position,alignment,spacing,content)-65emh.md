# annotation(position:alignment:spacing:content:)

**Framework**: Swift Charts  
**Kind**: method  
**Role**: Instance Method

Annotates this mark or collection of marks with a view positioned relative to its bounds.

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
func annotation<C>(position: AnnotationPosition = .automatic, alignment: Alignment = .center, spacing: CGFloat? = nil, @ViewBuilder content: () -> C) -> some ChartContent where C : View
```

## Parameters

- `position`: The location relative to the item being annotated at which the annotation will be placed.
- `alignment`: The guide for aligning the annotation in the specified position.
- `spacing`: Distance between the annotation and the annotated content, or `nil` if you want to use the default distance.
- `content`: A view builder that creates the annotation. The builder takes one input which provides information regarding the item being annotated such as its size.

## See Also

### Annotating marks
- [func annotation<C>(position: AnnotationPosition, alignment: Alignment, spacing: CGFloat?, content: (AnnotationContext) -> C) -> some ChartContent](./annotation%28position,alignment,spacing,content%29-26b2f.md)
  Annotates this mark or collection of marks with a view positioned relative to its bounds.
- [func annotation<C>(position: AnnotationPosition, alignment: Alignment, spacing: CGFloat?, overflowResolution: AnnotationOverflowResolution, content: () -> C) -> some ChartContent](./annotation%28position,alignment,spacing,overflowresolution,content%29-1kiow.md)
  Annotates this mark or collection of marks with a view positioned relative to its bounds.
- [func annotation<C>(position: AnnotationPosition, alignment: Alignment, spacing: CGFloat?, overflowResolution: AnnotationOverflowResolution, content: (AnnotationContext) -> C) -> some ChartContent](./annotation%28position,alignment,spacing,overflowresolution,content%29-6w4p3.md)
  Annotates this mark or collection of marks with a view positioned relative to its bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent/annotation(position:alignment:spacing:content:)-65emh)*