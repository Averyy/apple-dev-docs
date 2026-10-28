# scaleEffect(_:anchor:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Scales this view’s rendered output by the given vertical and horizontal size amounts, relative to an anchor point.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func scaleEffect(_ scale: CGSize, anchor: UnitPoint = .center) -> some View
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func scaleEffect(_ s: CGFloat, anchor: UnitPoint3D = .center) -> some View
```

```swift
@export(implementation)
nonisolated func scaleEffect(_ scale: Size3D, anchor: UnitPoint3D = .center) -> some View
```

```swift
nonisolated
func scaleEffect(_ s: CGFloat, anchor: UnitPoint = .center) -> ModifiedContent<Self, _UniformScaleEffect>
```

```swift
nonisolated
func scaleEffect(_ s: CGFloat, anchor: UnitPoint = .center) -> some View
```

## Discussion

Use `scaleEffect(_:anchor:)` to scale a view by applying a scaling transform of a specific size, specified by `scale`.

```swift
Image(systemName: "envelope.badge.fill")
    .resizable()
    .frame(width: 100, height: 100, alignment: .center)
    .foregroundColor(Color.red)
    .scaleEffect(CGSize(x: 0.9, y: 1.3), anchor: .leading)
    .border(Color.gray)
```

![A screenshot showing a red envelope scaled to a size of 90x130](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-View-scaleEffect@2x.png)

## Parameters

- `scale`: A [`CGSize`](../../CoreFoundation/cgsize.md) that represents the horizontal and vertical amount to scale the view.
- `anchor`: The point with a default of [`center`](../unitpoint/center.md) that defines the location within the view from which to apply the transformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/scaleeffect(_:anchor:)-7q7as)*