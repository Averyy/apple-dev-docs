# selectedAnnotations

**Framework**: MapKit  
**Kind**: property

The selected annotations.

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
var selectedAnnotations: [any MKAnnotation] { get set }
```

#### Discussion

Assigning a new array to this property selects only the first annotation in the array.

## See Also

- [var annotationVisibleRect: CGRect](mkmapview/annotationvisiblerect.md)
  The visible rectangle where the map is displaying annotation views.
- [func selectAnnotation(any MKAnnotation, animated: Bool)](mkmapview/selectannotation(_:animated:).md)
  Selects the specified annotation and displays a callout view for it.
- [func deselectAnnotation((any MKAnnotation)?, animated: Bool)](mkmapview/deselectannotation(_:animated:).md)
  Deselects the specified annotation and hides its callout view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/selectedannotations)*