# zIndex(_:)

**Framework**: RealityKit  
**Kind**: method

Controls the display order of overlapping views.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func zIndex(_ value: Double) -> some View
```

#### Discussion

Use `zIndex(_:)` when you want to control the front-to-back ordering of views.

In this example there are two overlapping rotated rectangles. The frontmost is represented by the larger index value.

```None
VStack {
    Rectangle()
        .fill(Color.yellow)
        .frame(width: 100, height: 100, alignment: .center)
        .zIndex(1) // Top layer.

    Rectangle()
        .fill(Color.red)
        .frame(width: 100, height: 100, alignment: .center)
        .rotationEffect(.degrees(45))
        // Here a zIndex of 0 is the default making
        // this the bottom layer.
}
```

## Parameters

- `value`: A relative front-to-back ordering for this view; the   default is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/resolvedmodel3d/zindex(_:))*