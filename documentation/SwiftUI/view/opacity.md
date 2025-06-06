# opacity(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the transparency of this view.

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
func opacity(_ opacity: Double) -> some View
```

#### Return Value

A view that sets the transparency of this view.

#### Discussion

Apply opacity to reveal views that are behind another view or to de-emphasize a view.

When applying the `opacity(_:)` modifier to a view that has already had its opacity transformed, the modifier multiplies the effect of the underlying opacity transformation.

The example below shows yellow and red rectangles configured to overlap. The top yellow rectangle has its opacity set to 50%, allowing the occluded portion of the bottom rectangle to be visible:

```swift
struct Opacity: View {
    var body: some View {
        VStack {
            Color.yellow.frame(width: 100, height: 100, alignment: .center)
                .zIndex(1)
                .opacity(0.5)

            Color.red.frame(width: 100, height: 100, alignment: .center)
                .padding(-40)
        }
    }
}
```

![Two overlaid rectangles, where the topmost has its opacity set to 50%,](https://docs-assets.developer.apple.com/published/317e3ae0fc1ddef46cb3052cd7840ff2/SwiftUI-View-opacity%402x.png)

## Parameters

- `opacity`: A value between 0 (fully transparent) and 1 (fully   opaque).

## See Also

- [func hidden() -> some View](view/hidden.md)
  Hides this view unconditionally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/opacity(_:))*