# selectAnnotation(_:animated:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

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
func selectAnnotation(_ annotation: any MKAnnotation, animated: Bool)
```

```objc
- (void) selectAnnotation:(id<MKAnnotation>) annotation animated:(BOOL) animated;
```

#### Discussion

If the specified annotation isn’t onscreen, and, therefore, doesn’t have an associated annotation view, this method has no effect.

## Parameters

- `annotation`: The annotation object to select.
- `animated`: If [`true`](../../Swift/true.md), the map view animates the callout view into position.

## See Also

### Managing annotation selections
- [var annotationVisibleRect: CGRect](./annotationvisiblerect.md)
  The visible rectangle where the map is displaying annotation views.
- [var selectedAnnotations: [any MKAnnotation]](./selectedannotations.md)
  The selected annotations.
- [func deselectAnnotation((any MKAnnotation)?, animated: Bool)](./deselectannotation%28_,animated%29.md)
  Deselects the specified annotation and hides its callout view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/selectannotation(_:animated:))*