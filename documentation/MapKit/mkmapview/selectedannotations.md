# selectedAnnotations

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

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
var selectedAnnotations: [any MKAnnotation] { get set }
```

```objc
@property (nonatomic, copy) NSArray<id<MKAnnotation>> * selectedAnnotations;
```

## Discussion

Assigning a new array to this property selects only the first annotation in the array.

## See Also

### Managing annotation selections
- [var annotationVisibleRect: CGRect](./annotationvisiblerect.md)
  The visible rectangle where the map is displaying annotation views.
- [func selectAnnotation(any MKAnnotation, animated: Bool)](./selectannotation%28_,animated%29.md)
  Selects the specified annotation and displays a callout view for it.
- [func deselectAnnotation((any MKAnnotation)?, animated: Bool)](./deselectannotation%28_,animated%29.md)
  Deselects the specified annotation and hides its callout view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/selectedannotations)*