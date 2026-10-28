# displayPriority

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The display priority of the annotation view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var displayPriority: MKFeatureDisplayPriority { get set }
```

```objc
@property (nonatomic) MKFeatureDisplayPriority displayPriority;
```

## Discussion

An annotation view with a priority of [`required`](../mkfeaturedisplaypriority/required.md) is always visible on the map, whereas other priorities may result in a hidden annotation view. Defaults to `required`.

## See Also

### Setting the priority for display
- [struct MKFeatureDisplayPriority](../mkfeaturedisplaypriority.md)
  Constants that indicates the display priority for annotations.
- [var zPriority: MKAnnotationViewZPriority](./zpriority.md)
  The relative importance of the annotation view when in an unselected state with respect to its ordering along the z-axis.
- [var selectedZPriority: MKAnnotationViewZPriority](./selectedzpriority.md)
  The relative importance of the annotation view when in a selected state with respect to its ordering along the z-axis.
- [struct MKAnnotationViewZPriority](../mkannotationviewzpriority.md)
  Constants that indicates the priority for ordering overlapping annotation views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/displaypriority)*