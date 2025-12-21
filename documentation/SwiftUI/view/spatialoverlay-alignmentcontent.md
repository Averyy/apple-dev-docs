# spatialOverlay(alignment:content:)

**Framework**: SwiftUI  
**Kind**: method

Adds secondary views within the 3D bounds of this view.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
nonisolated
func spatialOverlay<V>(alignment: Alignment3D = .center, @ViewBuilder content: () -> V) -> some View where V : View
```

#### Return Value

A view that adds `content` within the view’s 3D bounds.

#### Discussion

Multiple views provided by `content` are stacked depthwise.

## Parameters

- `alignment`: The alignment with a default value of    that you use to position the secondary view.
- `content`: The view builder which produces views to occupy the same 3D   space as this view. Multiple views provided by content are organized   into a  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/spatialoverlay(alignment:content:))*