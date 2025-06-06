# padding3D(_:_:)

**Framework**: App Intents  
**Kind**: method

Pads this view using the edge insets you specify.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
func padding3D(_ edges: Edge3D.Set = .all, _ length: CGFloat? = nil) -> some View
```

#### Return Value

A view that pads this view using edge the insets you specify.

## Parameters

- `edges`: The set of edges along which to inset this view.
- `length`: The amount to inset this view on each edge. If  ,   the amount is the system default amount.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/padding3d(_:_:))*