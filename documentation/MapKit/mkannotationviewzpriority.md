# MKAnnotationViewZPriority

**Framework**: MapKit  
**Kind**: struct

Constants that indicates the priority for ordering overlapping annotation views.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct MKAnnotationViewZPriority
```

## Topics

### Priorities
- [static let defaultSelected: MKAnnotationViewZPriority](mkannotationviewzpriority/defaultselected.md)
  The default view overlapping priority for a selected view.
- [static let defaultUnselected: MKAnnotationViewZPriority](mkannotationviewzpriority/defaultunselected.md)
  The default view overlapping priority for an unselected view.
- [static let max: MKAnnotationViewZPriority](mkannotationviewzpriority/max.md)
  The maximum allowed priority for overlapping views.
- [static let min: MKAnnotationViewZPriority](mkannotationviewzpriority/min.md)
  The minimum allowed priority for overlapping views.
### Initializers
- [init(Float)](mkannotationviewzpriority/init(_:).md)
  Creates an overlapping priority from the value.
- [init(rawValue: Float)](mkannotationviewzpriority/init(rawvalue:).md)
  Creates an overlapping priority from the value.

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
- [struct MKFeatureDisplayPriority](mkfeaturedisplaypriority.md)
  Constants that indicates the display priority for annotations.
- [var zPriority: MKAnnotationViewZPriority](mkannotationview/zpriority.md)
  The relative importance of the annotation view when in an unselected state with respect to its ordering along the z-axis.
- [var selectedZPriority: MKAnnotationViewZPriority](mkannotationview/selectedzpriority.md)
  The relative importance of the annotation view when in a selected state with respect to its ordering along the z-axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationviewzpriority)*