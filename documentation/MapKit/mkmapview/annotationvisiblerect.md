# annotationVisibleRect

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

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
var annotationVisibleRect: CGRect { get }
```

```objc
@property (nonatomic, readonly) CGRect annotationVisibleRect;
```

## See Also

### Managing annotation selections
- [var selectedAnnotations: [any MKAnnotation]](./selectedannotations.md)
  The selected annotations.
- [func selectAnnotation(any MKAnnotation, animated: Bool)](./selectannotation%28_,animated%29.md)
  Selects the specified annotation and displays a callout view for it.
- [func deselectAnnotation((any MKAnnotation)?, animated: Bool)](./deselectannotation%28_,animated%29.md)
  Deselects the specified annotation and hides its callout view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/annotationvisiblerect)*