# scaleEffect(_:anchor:)

**Framework**: MusicKit  
**Kind**: method

Scales this view’s rendered output by the given amount in both the horizontal and vertical directions, relative to an anchor point.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func scaleEffect(_ s: CGFloat, anchor: UnitPoint = .center) -> some View
```

#### Discussion

Use `scaleEffect(_:anchor:)` to apply a horizontally and vertically scaling transform to a view.

```swift
Image(systemName: "envelope.badge.fill")
    .resizable()
    .frame(width: 100, height: 100, alignment: .center)
    .foregroundColor(Color.red)
    .scaleEffect(2, anchor: .leading)
    .border(Color.gray)
```

## Parameters

- `s`: The amount to scale the view in the view in both the horizontal   and vertical directions.
- `anchor`: The anchor point with a default of   that   indicates the starting position for the scale operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/scaleeffect(_:anchor:)-7mj03)*