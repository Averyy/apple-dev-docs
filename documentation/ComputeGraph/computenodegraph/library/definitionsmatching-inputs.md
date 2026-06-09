# definitionsMatching(inputs:)

**Framework**: ComputeGraph  
**Kind**: method

Returns all definitions whose user-editable inputs, in order, match the given value types.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
final func definitionsMatching(inputs inputTypes: [ComputeNodeGraph.ValueType]) -> [ComputeNodeGraph.NodeDefinition]
```

#### Discussion

Non-user-editable inputs (framework-injected contexts, state bindings, etc.) are skipped when comparing the input sequence — callers pass only the user-visible types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/library/definitionsmatching(inputs:))*