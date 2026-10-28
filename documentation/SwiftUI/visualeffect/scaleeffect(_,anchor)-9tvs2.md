# scaleEffect(_:anchor:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Scales the view’s rendered output by the given vertical and horizontal size amounts, relative to an anchor point.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func scaleEffect(_ scale: CGSize, anchor: UnitPoint = .center) -> some VisualEffect
```

**Other overloads**:

```swift
@export(implementation)
func scaleEffect(_ s: CGFloat, anchor: UnitPoint3D = .center) -> some VisualEffect
```

```swift
@export(implementation)
func scaleEffect(_ scale: Size3D, anchor: UnitPoint3D = .center) -> some VisualEffect
```

```swift
func scaleEffect(_ scale: CGFloat, anchor: UnitPoint = .center) -> some VisualEffect
```

## Return Value

An effect that scales the view’s rendered output.

## Parameters

- `scale`: A [`CGSize`](../../CoreFoundation/cgsize.md) that represents the horizontal and vertical amount to scale the view.
- `anchor`: The point with a default of [`center`](../unitpoint/center.md) that defines the location within the view from which to apply the transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visualeffect/scaleeffect(_:anchor:)-9tvs2)*