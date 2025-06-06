# annotationVisibleRect

**Framework**: MapKit  
**Kind**: property

The visible rectangle where the map is displaying annotation views.

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
var annotationVisibleRect: CGRect { get }
```

## See Also

- [var selectedAnnotations: [any MKAnnotation]](mkmapview/selectedannotations.md)
  The selected annotations.
- [func selectAnnotation(any MKAnnotation, animated: Bool)](mkmapview/selectannotation(_:animated:).md)
  Selects the specified annotation and displays a callout view for it.
- [func deselectAnnotation((any MKAnnotation)?, animated: Bool)](mkmapview/deselectannotation(_:animated:).md)
  Deselects the specified annotation and hides its callout view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/annotationvisiblerect)*