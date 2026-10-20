# init(url:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Loads and displays a model from the specified URL.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(url: URL) where Content == ResolvedModel3D
```

#### Discussion

Until the model loads, SwiftUI displays a default placeholder. When the load operation completes successfully, SwiftUI updates the view to show the loaded model. If the operation fails, SwiftUI continues to display the placeholder. The following example loads and displays a model from an example server:

```swift
Model3D(url: URL(string: "https://example.com/robot.usdz")!)
```

If you want to customize the placeholder or apply [`Model3D`](../model3d.md)-specific modifiers — like `ResolvedModel3D/resizable()` — to the loaded model, use the [`init(url:content:placeholder:)`](./init%28url,content,placeholder%29.md) initializer instead.

## Parameters

- `url`: The URL of the model to display.

## See Also

### Creating a Model3D
- [init(named: String, bundle: Bundle?)](./init%28named,bundle%29.md)
  Loads and displays a model by name, by searching through the specified `Foundation/Bundle`.
- [init<Model, Placeholder>(named: String, bundle: Bundle?, content: (ResolvedModel3D) -> Model, placeholder: () -> Placeholder)](./init%28named,bundle,content,placeholder%29.md)
  Loads and displays a modifiable model by name, by searching through the specified [`Bundle`](../../Foundation/bundle.md), using a custom placeholder until the model loads.
- [init(named: String, bundle: Bundle?, transaction: Transaction, content: (Model3DPhase) -> Content)](./init%28named,bundle,transaction,content%29.md)
  Loads and displays a modifiable model by name, by searching through the specified [`Bundle`](../../Foundation/bundle.md), in phases.
- [init<Model, Placeholder>(url: URL, content: (ResolvedModel3D) -> Model, placeholder: () -> Placeholder)](./init%28url,content,placeholder%29.md)
  Loads and displays a modifiable model from the specified URL using a custom placeholder until the model loads.
- [init(url: URL, transaction: Transaction, content: (Model3DPhase) -> Content)](./init%28url,transaction,content%29.md)
  Loads and displays a modifiable model from the specified URL in phases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3d/init(url:))*