# frame(depth:alignment:)

**Framework**: RealityKit  
**Kind**: method

Positions this view within an invisible frame with the specified depth.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
func frame(depth: CGFloat?, alignment: DepthAlignment = .center) -> some View
```

#### Return Value

A view with a fixed dimension of `depth` if non-`nil`.

#### Discussion

Use this method to specify a fixed size for a view’s depth. If you don’t specify a dimension, the resulting view assumes this view’s sizing behavior in depth.

## Parameters

- `depth`: A fixed depth for the resulting view. If   is  ,   the resulting view assumes this view’s sizing behavior.
- `alignment`: The alignment of this view inside the resulting view.    applies if this view is smaller than the size given by   the resulting frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/frame(depth:alignment:))*