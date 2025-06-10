# preferredWindowClippingMargins(_:_:)

**Framework**: App Intents  
**Kind**: method

Requests additional margins for drawing beyond the bounds of the window.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func preferredWindowClippingMargins(_ edges: Edge3D.Set = .all, _ length: CGFloat?) -> some View
```

#### Discussion

This modifier will only have an effect on windows with a `.volumetric` window style.

A window’s bounds are based on its content, and resizable by dragging the corners. By default, the system clips any content that draws beyond the bounds. This modifier requests additional space for drawing outside the window’s bounds. Use this space to render extra visual effects that enhance the impact of your app. This content does not receive events, and may be clipped by the system at any time.

The additional margins granted by this modifier are not guaranteed, and the system may update or reduce them. Any time the system updates the current margins, it will update the `windowClippingMargins` value in the environment.

If multiple views request margins, the scene’s preferred margins will be the maximum preferred value for each face. For example, if one view wants a leading margin of `400` and another view a trailing margin of `400`, the scene will request both a leading and trailing margin of `400`. If one view requests a leading margin of `200` and another view a leading margin of `300`, the scene will request `300`.

## Parameters

- `edges`: The edges that should receive margins.
- `length`: The amount of margin requested on each specified edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/preferredwindowclippingmargins(_:_:)-ijji)*