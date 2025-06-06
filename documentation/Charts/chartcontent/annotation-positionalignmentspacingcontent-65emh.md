# annotation(position:alignment:spacing:content:)

**Framework**: Swift Charts  
**Kind**: method

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

- `position`: The location relative to the item being annotated at which   the annotation will be placed.
- `alignment`: The guide for aligning the annotation in the specified position.
- `spacing`: Distance between the annotation and the annotated content, or   if   you want to use the default distance.
- `content`: A view builder that creates the annotation.   The builder takes one input which provides information regarding the item being annotated   such as its size.

## See Also

- [func annotation<C>(position: AnnotationPosition, alignment: Alignment, spacing: CGFloat?, content: (AnnotationContext) -> C) -> some ChartContent](chartcontent/annotation(position:alignment:spacing:content:)-26b2f.md)
  Annotates this mark or collection of marks with a view positioned relative to its bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent/annotation(position:alignment:spacing:content:)-65emh)*