# removeAllBehaviors()

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Removes all individual behaviors from the composite behavior.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func removeAllBehaviors()
```

```objc
- (void) removeAllBehaviors;
```

## See Also

### Managing the Individual Behaviors in a Composite Behavior
- [func setWeight(Float, for: GKBehavior)](./setweight%28_,for%29.md)
  Sets the weight for the specified individual behavior’s influence on agents, adding that behavior to the composite behavior if it is not already present.
- [func weight(for: GKBehavior) -> Float](./weight%28for%29.md)
  Returns the weight for the specified individual behavior’s influence on agents.
- [func remove(GKBehavior)](./remove%28_%29.md)
  Removes the specified individual behavior from the composite behavior.
- [var behaviorCount: Int](./behaviorcount.md)
  The number of individual behaviors in the composite behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcompositebehavior/removeallbehaviors())*