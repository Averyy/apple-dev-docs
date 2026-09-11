# definitionsMatching(inputs:)

**Framework**: Compute Graph  
**Kind**: method

Returns all definitions whose user-editable inputs, in order, match the given value types.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro ?+

## Declaration

```swift
final func definitionsMatching(inputs inputTypes: [ComputeNodeGraph.ValueType]) -> [ComputeNodeGraph.NodeDefinition]
```

#### Discussion

Non-user-editable inputs (framework-injected contexts, state bindings, etc.) are skipped when comparing the input sequence — callers pass only the user-visible types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/library/definitionsmatching(inputs:))*