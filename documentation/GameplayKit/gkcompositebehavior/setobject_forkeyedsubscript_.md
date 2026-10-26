# setObject:forKeyedSubscript:

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Sets the weight for the behavior specified by subscript syntax.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setObject:(NSNumber *) weight forKeyedSubscript:(GKBehavior *) behavior;
```

#### Discussion

This method is equivalent to the [`setWeight(_:for:)`](./setweight%28_,for%29.md) method, but allows access using subscript syntax. Like that method, setting a weight by subscript adds the specified individual behavior to the composite behavior if the behavior is not already present.

## Parameters

- `weight`: A weight to be applied to the individual behavior’s influence on an agent’s speed and direction.
- `behavior`: A behavior object.

## See Also

### Working with Behaviors Using Subscript Syntax
- [subscript(GKBehavior) -> NSNumber](./subscript%28_%29-6jng9.md)
  Returns the weight associated with the behavior specified by subscript syntax.
- [subscript(Int) -> GKBehavior](./subscript%28_%29-6krdg.md)
  Returns the individual behavior at the specified index in the composite behavior’s list of behaviors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcompositebehavior/setobject:forkeyedsubscript:)*