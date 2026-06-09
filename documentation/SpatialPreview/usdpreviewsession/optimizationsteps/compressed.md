# compressed

**Framework**: Spatial Preview  
**Kind**: property

Allows the USD stage’s textures and meshes to be compressed before previewing on a device. Reduces the transmission file size of the USD stage by compressing textures and meshes to minimize the data sent, and is only applied when the stage exceeds the compression threshold. Can be combined with `.optimized` — compression runs after the `.optimized` optimization step on the resulting stage.

**Availability**:
- macOS 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
static let compressed: USDPreviewSession.OptimizationSteps
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatialpreview/usdpreviewsession/optimizationsteps/compressed)*