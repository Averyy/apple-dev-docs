# UIArrangementViewController.Arrangement

**Framework**: UIKit  
**Kind**: protocol

A type that describes how an arrangement view controller lays out its view controllers.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
protocol Arrangement
```

## Topics

### Getting the default view properties
- [var defaultViewProperties: Self.ViewProperties](uiarrangementviewcontroller/arrangement/defaultviewproperties.md)
  The default view properties for a view controller placed in the arrangement.
- [associatedtype ViewProperties](uiarrangementviewcontroller/arrangement/viewproperties.md)
  The type of properties for views within the arrangement.
### Setting view properties
- [func setViewProperties(Self.ViewProperties, for: UIArrangementViewController.ViewPlacement)](uiarrangementviewcontroller/arrangement/setviewproperties(_:for:).md)
  Sets the view properties for a placement in the arrangement.
### Getting a default arrangement
- [static var overlay: UIOverlayArrangement](uiarrangementviewcontroller/arrangement/overlay.md)
  The default overlay arrangement.
- [static var split: UISplitArrangement](uiarrangementviewcontroller/arrangement/split.md)
  The default split arrangement.

## Relationships

### Conforming Types
- [UIOverlayArrangement](uioverlayarrangement-swift.struct.md)
- [UISplitArrangement](uisplitarrangement-swift.struct.md)

## See Also

- [struct UIOverlayArrangement](uioverlayarrangement-swift.struct.md)
  An arrangement that overlays views.
- [struct UISplitArrangement](uisplitarrangement-swift.struct.md)
  An arrangement that splits views.
- [func updateArrangement<A>(A, animated: Bool)](uiarrangementviewcontroller/updatearrangement(_:animated:).md)
  Updates the arrangement of the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiarrangementviewcontroller/arrangement)*