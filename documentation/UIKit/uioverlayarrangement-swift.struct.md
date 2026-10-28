# UIOverlayArrangement

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

An arrangement that layers the primary view over the secondary view, or places the views side by side on a folded display.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
struct UIOverlayArrangement
```

## Overview

An overlay arrangement view controller places a primary view controller and a secondary view controller in a stacked arrangement when the device has a flat display, or next to each other horizontally when someone is holding a folded device in landscape orientation or above and below each other when someone is holding a folded device in portrait orientation. Here’s how the overlay arrangement positions the primary and secondary views:

- In a stacked overlay arrangement, the arrangement places the primary view above the secondary view in the z-axis.
- When someone holds a folded iPhone Duo in landscape orientation, the arrangement places the secondary view in the leading position and the primary view in the trailing position.
- When someone holds a folded iPhone Duo in portrait orientation, the arrangement places the secondary view in the top position and the primary view in the bottom position.

Create an overlay arrangement view controller by specifying a primary and secondary view controller, and call the [`updateArrangement(_:animated:)`](./uiarrangementviewcontroller/updatearrangement%28_,animated%29.md) method with [`overlay`](./uiarrangementviewcontroller/arrangement/overlay.md):

```swift
let arrangementVC = UIArrangementViewController()

let primaryVC = PrimaryViewController()
arrangementVC.setViewController(primaryVC, for: .primary)

let secondaryVC = SecondaryViewController()
arrangementVC.setViewController(secondaryVC, for: .secondary)

arrangementVC.updateArrangement(.overlay)
```

### Limit an overlay arrangement by orientation

You can limit which axes your overlay arrangement view controller supports by specifying the axes for the arrangement. The following example shows an arrangement that only functions vertically:

```swift
let arrangementVC = UIArrangementViewController()

let primaryVC = PrimaryViewController()
arrangementVC.setViewController(primaryVC, for: .primary)

let secondaryVC = SecondaryViewController()
arrangementVC.setViewController(secondaryVC, for: .secondary)

arrangementVC.updateArrangement(.overlay.axes(.vertical))
```

Use [`axes(_:)`](./uioverlayarrangement-swift.struct/axes%28_%29.md) to set the axes for an overlay arrangement. For axes that you don’t include, the arrangement view only displays the primary view.

### Customize a folded layout

You can adjust how the overlay arrangement positions the primary and secondary views on a folded iPhone Duo with view properties. For example, if you would prefer the primary view to appear in the leading position instead of the trailing position when someone holds a folded iPhone Duo in landscape orientation, customize the overlay arrangement with view properties.

Start by creating a [`UIOverlayArrangement`](./uioverlayarrangement-swift.struct.md) instance and a view properties instance:

```swift
var overlayArrangement = UIOverlayArrangement.overlay
var primaryViewProperties = overlayArrangement.defaultViewProperties
```

Specify an edge for the `edge` property, and then update the overlay arrangement and arrangement view:

```swift
primaryViewProperties.edge = .leading
overlayArrangement.setViewProperties(primaryViewProperties, for: .primary)
arrangementView.updateArrangement(overlayArrangement)
```

## Topics

### Creating an overlay arrangement
- [init()](./uioverlayarrangement-swift.struct/init%28%29.md)
  Creates an overlay arrangement.
### Configuring the arrangement
- [func axes(UIAxis) -> UIOverlayArrangement](./uioverlayarrangement-swift.struct/axes%28_%29.md)
  Sets the axes that the arrangement supports to the axes you provide.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [UIArrangementViewController.Arrangement](./uiarrangementviewcontroller/arrangement.md)

## See Also

### Configuring the arrangement
- [struct UISplitArrangement](./uisplitarrangement-swift.struct.md)
  An arrangement that places the primary and secondary views side by side along one or more axes.
- [UIArrangementViewController.Arrangement](./uiarrangementviewcontroller/arrangement.md)
  A type that describes how an arrangement view controller lays out its view controllers.
- [func updateArrangement<A>(A, animated: Bool)](./uiarrangementviewcontroller/updatearrangement%28_,animated%29.md)
  Updates the arrangement of the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uioverlayarrangement-swift.struct)*