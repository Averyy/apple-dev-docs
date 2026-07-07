# parameterNames

**Framework**: RealityKit  
**Kind**: property

The names of all parameters declared by the graph definition.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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