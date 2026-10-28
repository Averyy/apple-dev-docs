# subscript(_:)

**Framework**: GameplayKit  
**Kind**: subscript  
**Role**: Instance Subscript

Returns the weight associated with the behavior specified by subscript syntax.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
subscript(behavior: GKBehavior) -> NSNumber { get set }
```

```objc
- (NSNumber *) objectForKeyedSubscript:(GKBehavior *) behavior;
```

## Return Value

The weight applied to that behavior’s influence on an agent’s speed and direction, or `0.0` if that behavior is not in the composite behavior.

## Discussion

This method is equivalent to the [`weight(for:)`](./weight%28for%29.md) method, but allows access using subscript syntax.

## Parameters

- `behavior`: An individual behavior already included in the composite behavior’s set of behaviors.

## See Also

### Working with Behaviors Using Subscript Syntax
- [subscript(Int) -> GKBehavior](./subscript%28_%29-6krdg.md)
  Returns the individual behavior at the specified index in the composite behavior’s list of behaviors.
- [- setObject:forKeyedSubscript:](./setobject_forkeyedsubscript_.md)
  Sets the weight for the behavior specified by subscript syntax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcompositebehavior/subscript(_:)-6jng9)*