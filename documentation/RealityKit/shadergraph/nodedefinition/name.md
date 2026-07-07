# name

**Framework**: RealityKit  
**Kind**: property

The unique identifier for this node definition.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var name: String { get }
```

#### Discussion

Names follow the MaterialX convention, encoding the functional operation, input types, and output type. For example, `ND_atan2_float` identifies the two-argument arctangent node whose output is a `float`.

Use this value to look up a specific definition via [`definition(named:)`](shadergraph/nodelibrary/definition(named:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/nodedefinition/name)*