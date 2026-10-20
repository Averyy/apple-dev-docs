# chart3DPose(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Associates a binding to be updated when the 3D chart’s pose is changed by an interaction.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func chart3DPose(_ pose: Binding<Chart3DPose>) -> some View
```

**Other overloads**:

```swift
nonisolated
func chart3DPose(_ pose: Chart3DPose) -> some View
```

## Parameters

- `pose`: The 3D chart’s current pose.

## See Also

### 3D configuration
- [func chart3DCameraProjection(Chart3DCameraProjection) -> some View](./chart3dcameraprojection%28_%29.md)
- [func chart3DRenderingStyle(Chart3DRenderingStyle) -> some View](./chart3drenderingstyle%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chart3dpose(_:))*