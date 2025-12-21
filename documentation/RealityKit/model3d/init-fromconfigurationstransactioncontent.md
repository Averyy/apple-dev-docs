# init(from:configurations:transaction:content:)

**Framework**: RealityKit  
**Kind**: init

Loads and displays a modifiable model using the provided `ConfigurationCatalog` and configuration choices in phases.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
nonisolated
init(from catalog: Entity.ConfigurationCatalog, configurations: [String : String]? = nil, transaction: Transaction = Transaction(), @ViewBuilder content: @escaping (Model3DPhase) -> Content)
```

#### Discussion

Before the load operation completes, the phase is [`Model3DPhase.empty`](model3dphase/empty.md). After the operation completes, the phase becomes either [`Model3DPhase.failure(_:)`](model3dphase/failure(_:).md) or [`Model3DPhase.success(_:)`](model3dphase/success(_:).md). In the first case, the phase’s [`error`](model3dphase/error.md) value indicates the reason for failure. In the second case, the phase’s [`model`](model3dphase/model.md) property contains the loaded model. Use the phase to drive the output of the `content` closure, which defines the view’s appearance:

```swift
    Model3D(from: myConfigurationCatalog, configurations: ["vibe": "relaxed"]) { phase in
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

- `catalog`: A collection of alternative representations for an entity.
- `configurations`: A dictionary of configuration choices the initializer applies as it loads the entity,   mapping the ID of a configuration set to the ID of a configuration within that set.
- `transaction`: The transaction to use when the phase changes.
- `content`: A closure that takes the load phase as an input, and   returns the view to display for the specified phase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3d/init(from:configurations:transaction:content:))*