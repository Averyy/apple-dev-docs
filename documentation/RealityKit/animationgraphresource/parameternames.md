# parameterNames

**Framework**: RealityKit  
**Kind**: property

The names of all parameters declared by the graph definition.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var parameterNames: [String] { get }
```

#### Discussion

Use this list to discover the parameters a graph exposes for runtime control. Set values for these parameters through the owning entity’s parameter binding rather than through the resource itself, so that any entity using the graph can drive it with values that match its own state:

```swift
entity.parameters["MoveSpeed"] = BindableValue(Float(1.0))
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphresource/parameternames)*