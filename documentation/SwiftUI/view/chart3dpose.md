# chart3DPose(_:)

**Framework**: SwiftUI  
**Kind**: method

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

## Parameters

- `pose`: The 3D chart’s current pose.

## See Also

- [func chart3DCameraProjection(Chart3DCameraProjection) -> some View](view/chart3dcameraprojection(_:).md)
- [func chart3DRenderingStyle(Chart3DRenderingStyle) -> some View](view/chart3drenderingstyle(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chart3dpose(_:))*