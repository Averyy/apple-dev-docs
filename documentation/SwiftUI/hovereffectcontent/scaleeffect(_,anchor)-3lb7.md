# scaleEffect(_:anchor:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Scales the view’s rendered output by the given vertical and horizontal size amounts, relative to an anchor point.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func scaleEffect(_ scale: CGSize, anchor: UnitPoint = .center) -> some HoverEffectContent
```

**Other overloads**:

```swift
func scaleEffect(_ scale: CGFloat, anchor: UnitPoint = .center) -> some HoverEffectContent
```

## Return Value

An effect that scales the view’s rendered output.

## Parameters

- `scale`: A [`CGSize`](../../CoreFoundation/cgsize.md) that represents the horizontal and vertical amount to scale the view.
- `anchor`: The point with a default of [`center`](../unitpoint/center.md) that defines the location within the view from which to apply the transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/hovereffectcontent/scaleeffect(_:anchor:)-3lb7)*