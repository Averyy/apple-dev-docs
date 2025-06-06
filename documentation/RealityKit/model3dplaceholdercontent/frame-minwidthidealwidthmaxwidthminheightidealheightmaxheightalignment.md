# frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)

**Framework**: RealityKit  
**Kind**: method

Positions this view within an invisible frame having the specified size constraints.

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
func frame(minWidth: CGFloat? = nil, idealWidth: CGFloat? = nil, maxWidth: CGFloat? = nil, minHeight: CGFloat? = nil, idealHeight: CGFloat? = nil, maxHeight: CGFloat? = nil, alignment: Alignment = .center) -> some View
```

#### Return Value

A view with flexible dimensions given by the call’s non-`nil` parameters.

#### Discussion

Always specify at least one size characteristic when calling this method. Pass `nil` or leave out a characteristic to indicate that the frame should adopt this view’s sizing behavior, constrained by the other non-`nil` arguments.

The size proposed to this view is the size proposed to the frame, limited by any constraints specified, and with any ideal dimensions specified replacing any corresponding unspecified dimensions in the proposal.

If no minimum or maximum constraint is specified in a given dimension, the frame adopts the sizing behavior of its child in that dimension. If both constraints are specified in a dimension, the frame unconditionally adopts the size proposed for it, clamped to the constraints. Otherwise, the size of the frame in either dimension is:

- If a minimum constraint is specified and the size proposed for the frame by the parent is less than the size of this view, the proposed size, clamped to that minimum.
- If a maximum constraint is specified and the size proposed for the frame by the parent is greater than the size of this view, the proposed size, clamped to that maximum.
- Otherwise, the size of this view.

## Parameters

- `minWidth`: The minimum width of the resulting frame.
- `idealWidth`: The ideal width of the resulting frame.
- `maxWidth`: The maximum width of the resulting frame.
- `minHeight`: The minimum height of the resulting frame.
- `idealHeight`: The ideal height of the resulting frame.
- `maxHeight`: The maximum height of the resulting frame.
- `alignment`: The alignment of this view inside the resulting frame.   Note that most alignment values have no apparent effect when the   size of the frame happens to match that of this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3dplaceholdercontent/frame(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:alignment:))*