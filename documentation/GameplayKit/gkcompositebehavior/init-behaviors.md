# init(behaviors:)

**Framework**: GameplayKit  
**Kind**: init

Creates a composite behavior from the specified individual behaviors.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(behaviors: [GKBehavior])
```

#### Return Value

A new behavior object. To assign a behavior to an agent, use the agent’s [`behavior`](gkagent/behavior.md) property.

#### Discussion

The new behavior contains the specified behaviors, each with a weight of `1.0`. To change an individual behavior’s weight after creating the composite behavior, keep a reference to that behavior and use the [`setWeight(_:for:)`](gkcompositebehavior/setweight(_:for:).md) method.

For more information, see [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Parameters

- `behaviors`: An array of behavior objects.

## See Also

- [convenience init(behaviors: [GKBehavior], andWeights: [NSNumber])](gkcompositebehavior/init(behaviors:andweights:).md)
  Creates a behavior with the specified behaviors and weights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcompositebehavior/init(behaviors:))*