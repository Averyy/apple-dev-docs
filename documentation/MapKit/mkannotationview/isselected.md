# isSelected

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the annotation view is in a selected state.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var isSelected: Bool { get set }
```

```objc
@property (nonatomic, getter=isSelected) BOOL selected;
```

#### Discussion

Don’t set the value of this property directly. If the property contains [`true`](../../Swift/true.md), the annotation view is displaying a callout.

## See Also

### Managing the selection state
- [func setSelected(Bool, animated: Bool)](./setselected%28_,animated%29.md)
  Sets the selection state of the annotation view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkannotationview/isselected)*