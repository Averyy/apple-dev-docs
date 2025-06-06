# init(behaviors:andWeights:)

**Framework**: GameplayKit  
**Kind**: init

Creates a behavior with the specified behaviors and weights.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(behaviors: [GKBehavior], andWeights weights: [NSNumber])
```

#### Return Value

A new behavior object. To assign a behavior to an agent, use the agent’s [`behavior`](gkagent/behavior.md) property.

## Parameters

- `behaviors`: An array of behavior objects.
- `weights`: An array of numbers, each of which is the weight to be applied to the behavior at the corresponding index in the   array.

## See Also

- [convenience init(behaviors: [GKBehavior])](gkcompositebehavior/init(behaviors:).md)
  Creates a composite behavior from the specified individual behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcompositebehavior/init(behaviors:andweights:))*