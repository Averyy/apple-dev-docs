# deselectAnnotation(_:animated:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

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
func deselectAnnotation(_ annotation: (any MKAnnotation)?, animated: Bool)
```

```objc
- (void) deselectAnnotation:(id<MKAnnotation>) annotation animated:(BOOL) animated;
```

## Parameters

- `annotation`: The annotation object to deselect.
- `animated`: If [`true`](../../Swift/true.md), the map view animates the callout view offscreen.

## See Also

### Managing annotation selections
- [var annotationVisibleRect: CGRect](./annotationvisiblerect.md)
  The visible rectangle where the map is displaying annotation views.
- [var selectedAnnotations: [any MKAnnotation]](./selectedannotations.md)
  The selected annotations.
- [func selectAnnotation(any MKAnnotation, animated: Bool)](./selectannotation%28_,animated%29.md)
  Selects the specified annotation and displays a callout view for it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/deselectannotation(_:animated:))*