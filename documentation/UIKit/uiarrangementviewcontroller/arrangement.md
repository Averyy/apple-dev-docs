# UIArrangementViewController.Arrangement

**Framework**: UIKit  
**Kind**: protocol

A type that describes how an arrangement view controller lays out its view controllers.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
protocol Arrangement
```

## Topics

### Getting arrangements
- [static var overlay: UIOverlayArrangement](uiarrangementviewcontroller/arrangement/overlay.md)
  An arrangement that layers the primary view over the secondary view, or places the views side by side on a folded display.
- [static var split: UISplitArrangement](uiarrangementviewcontroller/arrangement/split.md)
  An arrangement that places the primary and secondary views side by side along one or more axes.
### Getting the default view properties
- [var defaultViewProperties: Self.ViewProperties](uiarrangementviewcontroller/arrangement/defaultviewproperties.md)
  The default view properties for a view controller placed in the arrangement.
- [associatedtype ViewProperties](uiarrangementviewcontroller/arrangement/viewproperties.md)
  Properties you use to customize how an arrangement presents views.
### Setting view properties
- [func setViewProperties(Self.ViewProperties, for: UIArrangementViewController.ViewPlacement)](uiarrangementviewcontroller/arrangement/setviewproperties(_:for:).md)
  Sets the view properties for a placement in the arrangement.

## Relationships

### Conforming Types
- [UIOverlayArrangement](uioverlayarrangement-swift.struct.md)
- [UISplitArrangement](uisplitarrangement-swift.struct.md)

## See Also

- [struct UIOverlayArrangement](uioverlayarrangement-swift.struct.md)
  An arrangement that layers the primary view over the secondary view, or places the views side by side on a folded display.
- [struct UISplitArrangement](uisplitarrangement-swift.struct.md)
  An arrangement that places the primary and secondary views side by side along one or more axes.
- [func updateArrangement<A>(A, animated: Bool)](uiarrangementviewcontroller/updatearrangement(_:animated:).md)
  Updates the arrangement of the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiarrangementviewcontroller/arrangement)*