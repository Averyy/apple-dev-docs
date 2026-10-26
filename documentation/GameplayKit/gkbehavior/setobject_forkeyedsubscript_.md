# setObject:forKeyedSubscript:

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Sets the weight for the goal specified by subscript syntax.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setObject:(NSNumber *) weight forKeyedSubscript:(GKGoal *) goal;
```

#### Discussion

This method is equivalent to the [`setWeight(_:for:)`](./setweight%28_,for%29.md) method, but allows access using subscript syntax. Like that method, setting a goal weight by subscript adds the specified goal to the behavior if not already present.

## Parameters

- `weight`: A weight to be applied to the goal’s influence on an agent’s speed and direction.
- `goal`: A goal object.

## See Also

### Working with Goals Using Subscript Syntax
- [subscript(GKGoal) -> NSNumber!](./subscript%28_%29-2yvko.md)
  Returns the weight associated with the goal specified by subscript syntax.
- [subscript(Int) -> GKGoal](./subscript%28_%29-997a9.md)
  Returns the goal at the specified index in the behavior’s list of goals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkbehavior/setobject:forkeyedsubscript:)*