# init(url:)

**Framework**: RealityKit  
**Kind**: init

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

If you want to customize the placeholder or apply [`Model3D`](model3d.md)-specific modifiers — like `ResolvedModel3D/resizable()` — to the loaded model, use the [`init(url:content:placeholder:)`](model3d/init(url:content:placeholder:).md) initializer instead.

## Parameters

- `url`: The URL of the model to display.

## See Also

- [init(named: String, bundle: Bundle?)](model3d/init(named:bundle:).md)
  Loads and displays a model by name, by searching through the specified `Foundation/Bundle`.
- [init<Model, Placeholder>(named: String, bundle: Bundle?, content: (ResolvedModel3D) -> Model, placeholder: () -> Placeholder)](model3d/init(named:bundle:content:placeholder:).md)
  Loads and displays a modifiable model by name, by searching through the specified [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle), using a custom placeholder until the model loads.
- [init(named: String, bundle: Bundle?, transaction: Transaction, content: (Model3DPhase) -> Content)](model3d/init(named:bundle:transaction:content:).md)
  Loads and displays a modifiable model by name, by searching through the specified [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle), in phases.
- [init<Model, Placeholder>(url: URL, content: (ResolvedModel3D) -> Model, placeholder: () -> Placeholder)](model3d/init(url:content:placeholder:).md)
  Loads and displays a modifiable model from the specified URL using a custom placeholder until the model loads.
- [init(url: URL, transaction: Transaction, content: (Model3DPhase) -> Content)](model3d/init(url:transaction:content:).md)
  Loads and displays a modifiable model from the specified URL in phases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3d/init(url:))*