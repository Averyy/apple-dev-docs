# UIOverlayArrangementViewProperties

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

Properties you use to customize how an overlay arrangement presents a view.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```objc
@interface UIOverlayArrangementViewProperties : NSObject
```

## Overview

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

### Creating view properties
- [- init](./uioverlayarrangementviewproperties/init.md)
  Creates a set of overlay arrangement view properties.
### Configuring the view
- [edge](./uioverlayarrangementviewproperties/edge.md)
  The edge the view occupies when the overlay arrangement transitions to a side-by-side layout.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)

## See Also

### Configuring the arrangement
- [axes](./uioverlayarrangement-c.class/axes.md)
  The supported axes of the arrangement.
- [defaultViewProperties](./uioverlayarrangement-c.class/defaultviewproperties.md)
  Returns the default properties for a view in the overlay arrangement.
- [- setViewProperties:forPlacement:](./uioverlayarrangement-c.class/setviewproperties_forplacement_.md)
  Sets the view properties in the overlay arrangement for a specific placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uioverlayarrangementviewproperties)*