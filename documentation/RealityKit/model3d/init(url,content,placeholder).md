# init(url:content:placeholder:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Loads and displays a modifiable model from the specified URL using a custom placeholder until the model loads.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<Model, Placeholder>(url: URL, @ViewBuilder content: @escaping (ResolvedModel3D) -> Model, @ViewBuilder placeholder: @escaping () -> Placeholder) where Content == Model3DPlaceholderContent<Model, Placeholder>, Model : View, Placeholder : View
```

#### Discussion

Until the model loads, `Model3D` displays the placeholder view that you specify. When the load operation completes successfully, `Model3D` updates the view to show content that you specify, which you create using the loaded model. For example, you can show a green placeholder, followed by a scaled version of the loaded model:

```swift
let url = URL(string: "https://example.com/robot.usdz")!
Model3D(url: url) { model in
    model.resizable()
} placeholder: {
    Color.green
}
```

If the load operation fails, `Model3D` continues to display the placeholder. To be able to display a different view on a load error, use the [`init(url:transaction:content:)`](./init%28url,transaction,content%29.md) initializer instead.

## Parameters

- `url`: The URL of the model to display.
- `content`: A closure that takes the loaded model as an input, and returns the view to show. You can return the model directly, or modify it as needed before returning it.
- `placeholder`: A closure that returns the view to show until the load operation completes successfully.

## See Also

### Creating a Model3D
- [init(named: String, bundle: Bundle?)](./init%28named,bundle%29.md)
  Loads and displays a model by name, by searching through the specified `Foundation/Bundle`.
- [init<Model, Placeholder>(named: String, bundle: Bundle?, content: (ResolvedModel3D) -> Model, placeholder: () -> Placeholder)](./init%28named,bundle,content,placeholder%29.md)
  Loads and displays a modifiable model by name, by searching through the specified [`Bundle`](../../Foundation/bundle.md), using a custom placeholder until the model loads.
- [init(named: String, bundle: Bundle?, transaction: Transaction, content: (Model3DPhase) -> Content)](./init%28named,bundle,transaction,content%29.md)
  Loads and displays a modifiable model by name, by searching through the specified [`Bundle`](../../Foundation/bundle.md), in phases.
- [init(url: URL)](./init%28url%29.md)
  Loads and displays a model from the specified URL.
- [init(url: URL, transaction: Transaction, content: (Model3DPhase) -> Content)](./init%28url,transaction,content%29.md)
  Loads and displays a modifiable model from the specified URL in phases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3d/init(url:content:placeholder:))*