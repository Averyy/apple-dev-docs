# aspectRatio(_:contentMode:)

**Framework**: RealityKit  
**Kind**: method

Constrains this view’s dimensions to the specified aspect ratio.

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
func aspectRatio(_ aspectRatio: CGFloat? = nil, contentMode: ContentMode) -> some View
```

#### Return Value

A view that constrains this view’s dimensions to the aspect ratio of the given size using `contentMode` as its scaling algorithm.

#### Discussion

Use `aspectRatio(_:contentMode:)` to constrain a view’s dimensions to an aspect ratio specified by a [`CGFloat`](https://developer.apple.com/documentation/CoreFoundation/CGFloat-swift.struct) using the specified content mode.

If this view is resizable, the resulting view will have `aspectRatio` as its aspect ratio. In this example, the purple ellipse has a 3:4 width-to-height ratio, and scales to fit its frame:

```None
Ellipse()
    .fill(Color.purple)
    .aspectRatio(0.75, contentMode: .fit)
    .frame(width: 200, height: 200)
    .border(Color(white: 0.75))
```

## Parameters

- `aspectRatio`: The ratio of width to height to use for the resulting   view. Use   to maintain the current aspect ratio in the   resulting view.
- `contentMode`: A flag that indicates whether this view fits or fills   the parent context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3dplaceholdercontent/aspectratio(_:contentmode:)-3u2a4)*