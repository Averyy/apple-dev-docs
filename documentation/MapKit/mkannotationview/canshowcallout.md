# canShowCallout

**Framework**: MapKit  
**Kind**: property

A Boolean value that indicates whether the annotation view is able to display extra information in a callout.

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
var canShowCallout: Bool { get set }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the map view shows a standard callout  when the user taps a selected annotation view. The callout uses the title and subtitle text from the associated annotation object. If there’s no title text, the map view treats the annotation view as if its [`isEnabled`](mkannotationview/isenabled.md) property is [`false`](https://developer.apple.com/documentation/Swift/false). The callout also displays any custom callout views in the [`leftCalloutAccessoryView`](mkannotationview/leftcalloutaccessoryview.md) and [`rightCalloutAccessoryView`](mkannotationview/rightcalloutaccessoryview.md) properties.

If the value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), the map view ignores the value of the title and subtitle strings, and the annotation view remains in an enabled state by default. You can still disable the view explicitly using the [`isEnabled`](mkannotationview/isenabled.md) property.

## See Also

- [var accessoryOffset: CGPoint](mkannotationview/accessoryoffset.md)
  An offset that changes the accessory’s default anchor point.
- [var leftCalloutAccessoryView: UIView?](mkannotationview/leftcalloutaccessoryview.md)
  The view to display on the left side of the standard callout.
- [var rightCalloutAccessoryView: UIView?](mkannotationview/rightcalloutaccessoryview.md)
  The view to display on the right side of the standard callout.
- [var detailCalloutAccessoryView: UIView?](mkannotationview/detailcalloutaccessoryview.md)
  The detail accessory view to use in the standard callout.
- [var leftCalloutOffset: CGPoint](mkannotationview/leftcalloutoffset.md)
  The offset in points from the middle-left of the annotation view.
- [var rightCalloutOffset: CGPoint](mkannotationview/rightcalloutoffset.md)
  The offset in points from the middle-right of the annotation view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/canshowcallout)*