# init(url:transaction:content:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Loads and displays a modifiable model from the specified URL in phases.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(url: URL, transaction: Transaction = Transaction(), @ViewBuilder content: @escaping (Model3DPhase) -> Content)
```

## Discussion

If you set the asynchronous model’s URL to `nil`, or after you set the URL to a value but before the load operation completes, the phase is [`Model3DPhase.empty`](../model3dphase/empty.md). After the operation completes, the phase becomes either [`Model3DPhase.failure(_:)`](../model3dphase/failure%28_%29.md) or [`Model3DPhase.success(_:)`](../model3dphase/success%28_%29.md). In the first case, the phase’s [`error`](../model3dphase/error.md) value indicates the reason for failure. In the second case, the phase’s [`model`](../model3dphase/model.md) property contains the loaded model. Use the phase to drive the output of the `content` closure, which defines the view’s appearance:

```swift
let url = URL(string: "https://example.com/robot.usdz")!
Model3D(url: url) { phase in
    if let model = phase.model {
        model // Displays the loaded model.
    } else if phase.error != nil {
        Color.red // Indicates an error.
    } else {
        Color.blue // Acts as a placeholder.
    }
}
```

To add transitions when you change the URL, apply an identifier to the [`Model3D`](../model3d.md).

## Parameters

- `url`: The URL of the image to display.
- `transaction`: The transaction to use when the phase changes.
- `content`: A closure that takes the load phase as an input, and returns the view to display for the specified phase.

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
- [init<Model, Placeholder>(url: URL, content: (ResolvedModel3D) -> Model, placeholder: () -> Placeholder)](./init%28url,content,placeholder%29.md)
  Loads and displays a modifiable model from the specified URL using a custom placeholder until the model loads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3d/init(url:transaction:content:))*