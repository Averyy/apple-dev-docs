# leftCalloutOffset

**Framework**: MapKit  
**Kind**: property

The offset in points from the middle-left of the annotation view.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+

## Declaration

```swift
@MainActor
var leftCalloutOffset: CGPoint { get set }
```

#### Discussion

This property specifies where the map view shows the anchor of the callout when it orients off the left side of the annotation view.

## See Also

- [var accessoryOffset: CGPoint](mkannotationview/accessoryoffset.md)
  An offset that changes the accessory’s default anchor point.
- [var canShowCallout: Bool](mkannotationview/canshowcallout.md)
  A Boolean value that indicates whether the annotation view is able to display extra information in a callout.
- [var leftCalloutAccessoryView: UIView?](mkannotationview/leftcalloutaccessoryview.md)
  The view to display on the left side of the standard callout.
- [var rightCalloutAccessoryView: UIView?](mkannotationview/rightcalloutaccessoryview.md)
  The view to display on the right side of the standard callout.
- [var detailCalloutAccessoryView: UIView?](mkannotationview/detailcalloutaccessoryview.md)
  The detail accessory view to use in the standard callout.
- [var rightCalloutOffset: CGPoint](mkannotationview/rightcalloutoffset.md)
  The offset in points from the middle-right of the annotation view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/leftcalloutoffset)*