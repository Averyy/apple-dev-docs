# optimized

**Framework**: Spatial Preview  
**Kind**: property

Allows the USD stage to be analyzed and potentially simplified or replaced with a proxy before previewing on a device. The USD analysis decides at runtime whether the stage can be passed as-is, simplified in place, or swapped for a lower-fidelity proxy based on scene complexity and session capabilities.

**Availability**:
- macOS 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
static let optimized: USDPreviewSession.OptimizationSteps
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/usdpreviewsession/optimizationsteps/optimized)*