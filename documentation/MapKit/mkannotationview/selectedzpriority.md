# selectedZPriority

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The relative importance of the annotation view when in a selected state with respect to its ordering along the z-axis.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var selectedZPriority: MKAnnotationViewZPriority { get set }
```

```objc
@property (nonatomic) MKAnnotationViewZPriority selectedZPriority;
```

## Discussion

The constant [`defaultSelected`](../mkannotationviewzpriority/defaultselected.md) is the default value for [`selectedZPriority`](./selectedzpriority.md).

## See Also

### Setting the priority for display
- [var displayPriority: MKFeatureDisplayPriority](./displaypriority.md)
  The display priority of the annotation view.
- [struct MKFeatureDisplayPriority](../mkfeaturedisplaypriority.md)
  Constants that indicates the display priority for annotations.
- [var zPriority: MKAnnotationViewZPriority](./zpriority.md)
  The relative importance of the annotation view when in an unselected state with respect to its ordering along the z-axis.
- [struct MKAnnotationViewZPriority](../mkannotationviewzpriority.md)
  Constants that indicates the priority for ordering overlapping annotation views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/selectedzpriority)*