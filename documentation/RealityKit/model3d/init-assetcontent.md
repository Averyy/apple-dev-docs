# init(asset:content:)

**Framework**: RealityKit  
**Kind**: init

**Availability**:
- visionOS 26.0+

## Declaration

```swift
nonisolated
init<Model>(asset: Model3DAsset, @ViewBuilder content: @escaping (ResolvedModel3D) -> Model) where Content == Model3DPlaceholderContent<Model, EmptyView>, Model : View
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3d/init(asset:content:))*