# UIOverlayArrangement

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An arrangement that layers the primary view over the secondary view, or places the views side by side on a folded display.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```objc
@interface UIOverlayArrangement : UIArrangement
```

## Overview

An overlay arrangement view controller places a primary view controller and a secondary view controller in a stacked arrangement when the device has a flat display, or next to each other horizontally when someone is holding a folded device in landscape orientation or above and below each other when someone is holding a folded device in portrait orientation. Here’s how the overlay arrangement positions the primary and secondary views:

- In a stacked overlay arrangement, the arrangement places the primary view above the secondary view in the z-axis.
- When someone holds a folded iPhone Duo in landscape orientation, the arrangement places the secondary view in the leading position and the primary view in the trailing position.
- When someone holds a folded iPhone Duo in portrait orientation, the arrangement places the secondary view in the top position and the primary view in the bottom position.

Create an overlay arrangement view controller by specifying a primary and secondary view controller, and call the [`updateArrangement:`](./uiarrangementviewcontroller/updatearrangement_.md) method with [`overlayArrangement`](./uioverlayarrangement-c.class/overlayarrangement.md):

```objc
self.arrangementVC = [[UIArrangementViewController alloc] init];

self.primaryVC = [[PrimaryController alloc] init];
[self.arrangementVC setViewController:self.primaryVC forPlacement:UIArrangementViewControllerViewPlacementPrimary];

self.secondaryVC = [[SecondaryController alloc] init];
[self.arrangementVC setViewController:self.secondaryVC forPlacement:UIArrangementViewControllerViewPlacementSecondary];

UIOverlayArrangement *arrangement = [UIOverlayArrangement overlayArrangement];
[self.arrangementVC updateArrangement:arrangement];
```

### Limit an overlay arrangement by orientation

You can limit which axes your overlay arrangement view controller supports by specifying the axes for the arrangement. The following example shows an arrangement that only splits vertically:

```objc
self.arrangementVC = [[UIArrangementViewController alloc] init];

self.primaryVC = [[PrimaryController alloc] init];
[self.arrangementVC setViewController:self.primaryVC forPlacement:UIArrangementViewControllerViewPlacementPrimary];

self.secondaryVC = [[SecondaryController alloc] init];
[self.arrangementVC setViewController:self.secondaryVC forPlacement:UIArrangementViewControllerViewPlacementSecondary];

UIOverlayArrangement *arrangement = [UIOverlayArrangement overlayArrangement];
arrangement.axes = UIAxisVertical;
[self.arrangementVC updateArrangement:arrangement];
```

Use [`axes`](./uioverlayarrangement-c.class/axes.md) to set the axes for an overlay arrangement. For axes that you don’t include, the arrangement view only displays the primary view.

### Customize a folded layout

You can adjust how the overlay arrangement positions the primary and secondary views on a folded iPhone Duo with view properties. For example, if you would prefer the primary view to appear in the leading position instead of the trailing position when someone holds a folded iPhone Duo in landscape orientation, customize the overlay arrangement with view properties.

Start by creating a [`UIOverlayArrangement`](./uioverlayarrangement-c.class.md) instance and a [`UIOverlayArrangementViewProperties`](./uioverlayarrangementviewproperties.md) instance:

```objc
UIOverlayArrangement *overlayArrangement = [UIOverlayArrangement overlayArrangement];
UIOverlayArrangementViewProperties *primaryViewProperties = [overlayArrangement.defaultViewProperties copy];
```

Specify an edge for the [`edge`](./uioverlayarrangementviewproperties/edge.md) property, and then update the overlay arrangement and arrangement view controller:

```objc
primaryViewProperties.edge = NSDirectionalRectEdgeLeading;
[overlayArrangement setViewProperties:primaryViewProperties forPlacement:UIArrangementViewControllerViewPlacementPrimary];
[arrangementViewController updateArrangement:overlayArrangement animated:NO];
```

## Topics

### Creating an overlay arrangement
- [+ overlayArrangement](./uioverlayarrangement-c.class/overlayarrangement.md)
  Returns an overlay arrangement.
### Configuring the arrangement
- [axes](./uioverlayarrangement-c.class/axes.md)
  The supported axes of the arrangement.
- [defaultViewProperties](./uioverlayarrangement-c.class/defaultviewproperties.md)
  Returns the default properties for a view in the overlay arrangement.
- [- setViewProperties:forPlacement:](./uioverlayarrangement-c.class/setviewproperties_forplacement_.md)
  Sets the view properties in the overlay arrangement for a specific placement.
- [UIOverlayArrangementViewProperties](./uioverlayarrangementviewproperties.md)
  Properties you use to customize how an overlay arrangement presents a view.

## Relationships

### Inherits From
- [UIArrangement](./uiarrangement.md)

## See Also

### Configuring the arrangement
- [UISplitArrangement](./uisplitarrangement-c.class.md)
  An arrangement that places the primary and secondary views side by side along one or more axes.
- [UIArrangement](./uiarrangement.md)
  A type that describes how an arrangement view controller lays out its view controllers.
- [- updateArrangement:](./uiarrangementviewcontroller/updatearrangement_.md)
  Updates the arrangement of the view controller.
- [- updateArrangement:animated:](./uiarrangementviewcontroller/updatearrangement_animated_.md)
  Updates the arrangement of the view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uioverlayarrangement-c.class)*