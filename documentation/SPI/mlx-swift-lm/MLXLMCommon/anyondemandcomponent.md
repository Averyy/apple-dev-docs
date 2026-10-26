---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/anyondemandcomponent"
framework: "mlx-swift-lm/MLXLMCommon"
---

# AnyOnDemandComponent

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

A model component that loads the first time it is used. See [`OnDemandComponent`](./ondemandcomponent.md).

## Declaration

```swift
class AnyOnDemandComponent
```

#### Overview

It lives outside the model’s module tree, so loading it does not change the model. It reads, verifies and evaluates the component under a load lock, and publishes it only after that. Concurrent first uses share one load. A published component does not change. State queries such as [`isLoaded`](./anyondemandcomponent/isloaded.md) never wait for a load in progress.

## Topics

### Instance Properties
- [let component: ModelComponent](./anyondemandcomponent/component.md)
- [var isLoaded: Bool](./anyondemandcomponent/isloaded.md)
  Whether the component has loaded.

## Relationships

### Inherited By
- [OnDemandComponent](./ondemandcomponent.md)
### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/anyondemandcomponent)*