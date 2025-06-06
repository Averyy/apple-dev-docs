# init(url:content:placeholder:)

**Framework**: RealityKit  
**Kind**: init

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

If the load operation fails, `Model3D` continues to display the placeholder. To be able to display a different view on a load error, use the [`init(url:transaction:content:)`](model3d/init(url:transaction:content:).md) initializer instead.

## Parameters

- `url`: The URL of the model to display.
- `content`: A closure that takes the loaded model as an input, and   returns the view to show. You can return the model directly, or   modify it as needed before returning it.
- `placeholder`: A closure that returns the view to show until the   load operation completes successfully.

## See Also

- [init(named: String, bundle: Bundle?)](model3d/init(named:bundle:).md)
  Loads and displays a model by name, by searching through the specified `Foundation/Bundle`.
- [init<Model, Placeholder>(named: String, bundle: Bundle?, content: (ResolvedModel3D) -> Model, placeholder: () -> Placeholder)](model3d/init(named:bundle:content:placeholder:).md)
  Loads and displays a modifiable model by name, by searching through the specified [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle), using a custom placeholder until the model loads.
- [init(named: String, bundle: Bundle?, transaction: Transaction, content: (Model3DPhase) -> Content)](model3d/init(named:bundle:transaction:content:).md)
  Loads and displays a modifiable model by name, by searching through the specified [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle), in phases.
- [init(url: URL)](model3d/init(url:).md)
  Loads and displays a model from the specified URL.
- [init(url: URL, transaction: Transaction, content: (Model3DPhase) -> Content)](model3d/init(url:transaction:content:).md)
  Loads and displays a modifiable model from the specified URL in phases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3d/init(url:content:placeholder:))*