# selectAnnotation(_:animated:)

**Framework**: MapKit  
**Kind**: method

Selects the specified annotation and displays a callout view for it.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func selectAnnotation(_ annotation: any MKAnnotation, animated: Bool)
```

#### Discussion

If the specified annotation isn’t onscreen, and, therefore, doesn’t have an associated annotation view, this method has no effect.

## Parameters

- `annotation`: The annotation object to select.
- `animated`: If  , the map view animates the callout view into position.

## See Also

- [var annotationVisibleRect: CGRect](mkmapview/annotationvisiblerect.md)
  The visible rectangle where the map is displaying annotation views.
- [var selectedAnnotations: [any MKAnnotation]](mkmapview/selectedannotations.md)
  The selected annotations.
- [func deselectAnnotation((any MKAnnotation)?, animated: Bool)](mkmapview/deselectannotation(_:animated:).md)
  Deselects the specified annotation and hides its callout view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/selectannotation(_:animated:))*