# detailCalloutAccessoryView

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The detail accessory view to use in the standard callout.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
var detailCalloutAccessoryView: UIView? { get set }
```

*macOS*

```swift
var detailCalloutAccessoryView: NSView? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, nullable) UIView * detailCalloutAccessoryView;
```

*macOS*

```objc
@property (nonatomic, strong, nullable) NSView * detailCalloutAccessoryView;
```

## See Also

### Managing callout views
- [var accessoryOffset: CGPoint](./accessoryoffset.md)
  An offset that changes the accessory’s default anchor point.
- [var canShowCallout: Bool](./canshowcallout.md)
  A Boolean value that indicates whether the annotation view is able to display extra information in a callout.
- [var leftCalloutAccessoryView: UIView?](./leftcalloutaccessoryview.md)
  The view to display on the left side of the standard callout.
- [var rightCalloutAccessoryView: UIView?](./rightcalloutaccessoryview.md)
  The view to display on the right side of the standard callout.
- [var leftCalloutOffset: CGPoint](./leftcalloutoffset.md)
  The offset in points from the middle-left of the annotation view.
- [var rightCalloutOffset: CGPoint](./rightcalloutoffset.md)
  The offset in points from the middle-right of the annotation view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/detailcalloutaccessoryview)*