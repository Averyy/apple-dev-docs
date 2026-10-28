# scaleEffect(_:anchor:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Scales this view’s rendered output by the given amount in both the horizontal and vertical directions, relative to an anchor point.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func scaleEffect(_ s: CGFloat, anchor: UnitPoint = .center) -> ModifiedContent<Self, _UniformScaleEffect>
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
func scaleEffect(_ s: CGFloat, anchor: UnitPoint = .center) -> some View
```

```swift
nonisolated
func scaleEffect(_ scale: CGSize, anchor: UnitPoint = .center) -> some View
```

## Discussion

Use `scaleEffect(_:anchor:)` to apply a horizontally and vertically scaling transform to a view.

```swift
Image(systemName: "envelope.badge.fill")
    .resizable()
    .frame(width: 100, height: 100, alignment: .center)
    .foregroundColor(Color.red)
    .scaleEffect(2, anchor: .leading)
    .border(Color.gray)
```

![A screenshot showing a 100x100 pixel red envelope scaled up to 2x the](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-View-scaleEffect-cgfloat@2x.png)

## Parameters

- `s`: The amount to scale the view in the view in both the horizontal and vertical directions.
- `anchor`: The anchor point with a default of [`center`](../unitpoint/center.md) that indicates the starting position for the scale operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/scaleeffect(_:anchor:)-8licv)*