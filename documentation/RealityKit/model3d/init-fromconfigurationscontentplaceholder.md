# init(from:configurations:content:placeholder:)

**Framework**: RealityKit  
**Kind**: init

Loads and displays a modifiable model using the provided `ConfigurationCatalog` and configuration choices using a custom placeholder until the model loads.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
init<Model, Placeholder>(from catalog: Entity.ConfigurationCatalog, configurations: [String : String]? = nil, @ViewBuilder content: @escaping (ResolvedModel3D) -> Model, @ViewBuilder placeholder: @escaping () -> Placeholder) where Content == Model3DPlaceholderContent<Model, Placeholder>, Model : View, Placeholder : View
```

#### Discussion

Until the model loads, [`Model3D`](model3d.md) displays the placeholder view that you specify. When the load operation completes successfully, SwiftUI updates the view to show content that you specify, which you create using the loaded model. For example, you can show a green placeholder, followed by a scaled version of the loaded model:

```swift
Model3D(
    from: myConfigurationCatalog,
    configurations: ["vibe": "relaxed"] ) { model in
    model.resizable()
} placeholder: {
    Color.green
}
```

If the load operation fails, [`Model3D`](model3d.md) continues to display the placeholder. To be able to display a different view on a load error, use the  [`init(from:configurations:transaction:content:)`](model3d/init(from:configurations:transaction:content:).md) initializer instead.

## Parameters

- `catalog`: A collection of alternative representations for an entity.
- `configurations`: A dictionary of configuration choices the initializer applies as it loads the entity,   mapping the ID of a configuration set to the ID of a configuration within that set.
- `content`: A closure that takes the loaded model as an input, and   returns the view to show. You can return the model directly, or   modify it as needed before returning it.
- `placeholder`: A closure that returns the view to show until the   load operation completes successfully.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3d/init(from:configurations:content:placeholder:))*