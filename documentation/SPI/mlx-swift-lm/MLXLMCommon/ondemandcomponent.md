---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/ondemandcomponent"
framework: "mlx-swift-lm/MLXLMCommon"
---

# OnDemandComponent

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

A model component of type `Content` that loads the first time it is used.

## Declaration

```swift
final class OnDemandComponent<Content> where Content : Module
```

## Mentions

- [Model Compatibility](./model-compatibility.md)

#### Overview

`Content` holds the component’s modules at the paths they have in the model:

```swift
private let vision = OnDemandComponent(.vision) { VisionStack(config) }

public var onDemandComponents: [AnyOnDemandComponent] { [vision] }

let stack = try vision.load()
```

## Topics

### Initializers
- [init(ModelComponent, make: @Sendable () -> Content)](./ondemandcomponent/init%28_,make%29.md)
### Instance Methods
- [func load() throws -> Content](./ondemandcomponent/load%28%29.md)
  The component’s modules, loaded on first use.

## Relationships

### Inherits From
- [AnyOnDemandComponent](./anyondemandcomponent.md)
### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/ondemandcomponent)*