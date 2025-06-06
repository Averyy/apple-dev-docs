# init(named:bundle:transaction:content:)

**Framework**: RealityKit  
**Kind**: init

Loads and displays a modifiable model by name, by searching through the specified [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle), in phases.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(named name: String, bundle: Bundle? = nil, transaction: Transaction = Transaction(), @ViewBuilder content: @escaping (Model3DPhase) -> Content)
```

#### Discussion

Before the load operation completes, the phase is [`Model3DPhase.empty`](model3dphase/empty.md). After the operation completes, the phase becomes either [`Model3DPhase.failure(_:)`](model3dphase/failure(_:).md) or [`Model3DPhase.success(_:)`](model3dphase/success(_:).md). In the first case, the phase’s [`error`](model3dphase/error.md) value indicates the reason for failure. In the second case, the phase’s [`model`](model3dphase/model.md) property contains the loaded model. Use the phase to drive the output of the `content` closure, which defines the view’s appearance:

```swift
    Model3D(named: "Robot-Drummer") { phase in
        if let model = phase.model {
            model // Displays the loaded model.
        } else if phase.error != nil {
            Color.red // Indicates an error.
        } else {
            Color.blue // Acts as a placeholder.
        }
    }
```

To add transitions when you change the name, apply an identifier to the [`Model3D`](model3d.md).

## Parameters

- `name`: The name of the USD or Reality file to display.
- `bundle`: The Bundle used to look up the model by name. If not   provided, defaults to the app’s main bundle.
- `transaction`: The transaction to use when the phase changes.
- `content`: A closure that takes the load phase as an input, and   returns the view to display for the specified phase.

## See Also

- [init(named: String, bundle: Bundle?)](model3d/init(named:bundle:).md)
  Loads and displays a model by name, by searching through the specified `Foundation/Bundle`.
- [init<Model, Placeholder>(named: String, bundle: Bundle?, content: (ResolvedModel3D) -> Model, placeholder: () -> Placeholder)](model3d/init(named:bundle:content:placeholder:).md)
  Loads and displays a modifiable model by name, by searching through the specified [`Bundle`](https://developer.apple.com/documentation/Foundation/Bundle), using a custom placeholder until the model loads.
- [init(url: URL)](model3d/init(url:).md)
  Loads and displays a model from the specified URL.
- [init<Model, Placeholder>(url: URL, content: (ResolvedModel3D) -> Model, placeholder: () -> Placeholder)](model3d/init(url:content:placeholder:).md)
  Loads and displays a modifiable model from the specified URL using a custom placeholder until the model loads.
- [init(url: URL, transaction: Transaction, content: (Model3DPhase) -> Content)](model3d/init(url:transaction:content:).md)
  Loads and displays a modifiable model from the specified URL in phases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3d/init(named:bundle:transaction:content:))*