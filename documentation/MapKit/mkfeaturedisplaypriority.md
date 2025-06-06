# MKFeatureDisplayPriority

**Framework**: MapKit  
**Kind**: struct

Constants that indicates the display priority for annotations.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct MKFeatureDisplayPriority
```

## Topics

### Priorities
- [static let required: MKFeatureDisplayPriority](mkfeaturedisplaypriority/required.md)
  A constant indicating that the item is required.
- [static let defaultHigh: MKFeatureDisplayPriority](mkfeaturedisplaypriority/defaulthigh.md)
  A constant indicating that the item’s display priority is high.
- [static let defaultLow: MKFeatureDisplayPriority](mkfeaturedisplaypriority/defaultlow.md)
  A constant indicating that the item’s display priority is low.
### Creating Feature Display Priorities
- [init(Float)](mkfeaturedisplaypriority/init(_:).md)
  Creates a feature display priority using the specified floating point value.
- [init(rawValue: Float)](mkfeaturedisplaypriority/init(rawvalue:).md)
  Creates a feature display priority using the specified raw floating point value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var displayPriority: MKFeatureDisplayPriority](mkannotationview/displaypriority.md)
  The display priority of the annotation view.
- [var zPriority: MKAnnotationViewZPriority](mkannotationview/zpriority.md)
  The relative importance of the annotation view when in an unselected state with respect to its ordering along the z-axis.
- [var selectedZPriority: MKAnnotationViewZPriority](mkannotationview/selectedzpriority.md)
  The relative importance of the annotation view when in a selected state with respect to its ordering along the z-axis.
- [struct MKAnnotationViewZPriority](mkannotationviewzpriority.md)
  Constants that indicates the priority for ordering overlapping annotation views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkfeaturedisplaypriority)*