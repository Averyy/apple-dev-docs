# pointerInteraction(_:styleFor:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for a pointer style after an interaction receives a new region.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
optional func pointerInteraction(_ interaction: UIPointerInteraction, styleFor region: UIPointerRegion) -> UIPointerStyle?
```

```objc
- (UIPointerStyle *) pointerInteraction:(UIPointerInteraction *) interaction styleForRegion:(UIPointerRegion *) region;
```

## Return Value

A `UIPointerStyle` describing the desired hover effect or pointer appearance for the given `UIPointerRegion`.

## Parameters

- `interaction`: This [`UIPointerInteraction`](../uipointerinteraction.md).
- `region`: The [`UIPointerRegion`](../uipointerregion.md) that represents the entire surface of the interaction’s view.

## See Also

### Defining pointer styles for regions
- [func pointerInteraction(UIPointerInteraction, regionFor: UIPointerRegionRequest, defaultRegion: UIPointerRegion) -> UIPointerRegion?](./pointerinteraction%28_,regionfor,defaultregion%29.md)
  Asks the delegate for a region as the pointer moves within the interaction’s view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerinteractiondelegate/pointerinteraction(_:stylefor:))*