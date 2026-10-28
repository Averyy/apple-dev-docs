# init(named:bundle:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Loads and displays a model by name, by searching through the specified `Foundation/Bundle`.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(named name: String, bundle: Bundle? = nil) where Content == ResolvedModel3D
```

## Discussion

Until the model loads, `Model3D` displays a default placeholder. When the load operation completes successfully, `Model3D` updates the view to show the loaded model. If the operation fails, `Model3D` continues to display the placeholder. The following example loads and displays a model from an example server:

```swift
Model3D(named: "Robot-Drummer")
```

If you want to customize the placeholder or apply [`ResolvedModel3D`](../resolvedmodel3d.md)-specific modifiers — like `ResolvedModel3D/resizable()` — to the loaded model, use the [`init(named:bundle:content:placeholder:)`](./init%28named,bundle,content,placeholder%29.md) initializer instead.

## Parameters

- `name`: The name of the USD or Reality file to display.
- `bundle`: The Bundle used to look up the model by name. If not provided, defaults to the app’s main bundle.

## See Also

### Creating a Model3D
- [init<Model, Placeholder>(named: String, bundle: Bundle?, content: (ResolvedModel3D) -> Model, placeholder: () -> Placeholder)](./init%28named,bundle,content,placeholder%29.md)
  Loads and displays a modifiable model by name, by searching through the specified [`Bundle`](../../Foundation/bundle.md), using a custom placeholder until the model loads.
- [init(named: String, bundle: Bundle?, transaction: Transaction, content: (Model3DPhase) -> Content)](./init%28named,bundle,transaction,content%29.md)
  Loads and displays a modifiable model by name, by searching through the specified [`Bundle`](../../Foundation/bundle.md), in phases.
- [init(url: URL)](./init%28url%29.md)
  Loads and displays a model from the specified URL.
- [init<Model, Placeholder>(url: URL, content: (ResolvedModel3D) -> Model, placeholder: () -> Placeholder)](./init%28url,content,placeholder%29.md)
  Loads and displays a modifiable model from the specified URL using a custom placeholder until the model loads.
- [init(url: URL, transaction: Transaction, content: (Model3DPhase) -> Content)](./init%28url,transaction,content%29.md)
  Loads and displays a modifiable model from the specified URL in phases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3d/init(named:bundle:))*