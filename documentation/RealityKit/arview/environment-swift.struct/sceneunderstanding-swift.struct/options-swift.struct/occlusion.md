# occlusion

**Framework**: RealityKit  
**Kind**: property

The `.occlusion` option means that the reconstructed geometry will be used for rendering, but only to update the depth buffer. Parts of virtual objects which are behind the reconstructed geometry are not rendered.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)

## Declaration

```swift
static let occlusion: ARView.Environment.SceneUnderstanding.Options
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/environment-swift.struct/sceneunderstanding-swift.struct/options-swift.struct/occlusion)*