# name

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The unique identifier for this node definition.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var name: String { get }
```

## Discussion

Names follow the MaterialX convention, encoding the functional operation, input types, and output type. For example, `ND_atan2_float` identifies the two-argument arctangent node whose output is a `float`.

Use this value to look up a specific definition via [`definition(named:)`](../nodelibrary/definition%28named%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/nodedefinition/name)*