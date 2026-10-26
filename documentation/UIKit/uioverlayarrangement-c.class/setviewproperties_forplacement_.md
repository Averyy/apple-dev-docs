# setViewProperties:forPlacement:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the view properties in the overlay arrangement for a specific placement.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```objc
- (void) setViewProperties:(UIOverlayArrangementViewProperties *) viewProperties forPlacement:(UIArrangementViewControllerViewPlacement) placement;
```

## Parameters

- `viewProperties`: The view properties in the arrangement.
- `placement`: The placement of the properties in the arrangement.

## See Also

### Configuring the arrangement
- [axes](./axes.md)
  The supported axes of the arrangement.
- [defaultViewProperties](./defaultviewproperties.md)
  Returns the default properties for a view in the overlay arrangement.
- [UIOverlayArrangementViewProperties](../uioverlayarrangementviewproperties.md)
  Properties you use to customize how an overlay arrangement presents a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uioverlayarrangement-c.class/setviewproperties:forplacement:)*