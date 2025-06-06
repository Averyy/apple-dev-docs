# deselectAnnotation(_:animated:)

**Framework**: MapKit  
**Kind**: method

Deselects the specified annotation and hides its callout view.

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
func deselectAnnotation(_ annotation: (any MKAnnotation)?, animated: Bool)
```

## Parameters

- `annotation`: The annotation object to deselect.
- `animated`: If  , the map view animates the callout view offscreen.

## See Also

- [var annotationVisibleRect: CGRect](mkmapview/annotationvisiblerect.md)
  The visible rectangle where the map is displaying annotation views.
- [var selectedAnnotations: [any MKAnnotation]](mkmapview/selectedannotations.md)
  The selected annotations.
- [func selectAnnotation(any MKAnnotation, animated: Bool)](mkmapview/selectannotation(_:animated:).md)
  Selects the specified annotation and displays a callout view for it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/deselectannotation(_:animated:))*