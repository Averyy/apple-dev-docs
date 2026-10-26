# subscript(_:)

**Framework**: GameplayKit  
**Kind**: subscript  
**Role**: Instance Subscript

Returns the individual behavior at the specified index in the composite behavior’s list of behaviors.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
subscript(idx: Int) -> GKBehavior { get }
```

```objc
- (GKBehavior *) objectAtIndexedSubscript:(NSUInteger) idx;
```

#### Return Value

The behavior at the specified index.

#### Discussion

The order of individual behaviors in a composite behavior is undefined. However, you can use this method to enumerate all individual behaviors in a composite behavior.

## Parameters

- `idx`: An index in the composite behavior’s list of individual behaviors; it must be less than the value of the [`behaviorCount`](./behaviorcount.md) property.

## See Also

### Working with Behaviors Using Subscript Syntax
- [subscript(GKBehavior) -> NSNumber](./subscript%28_%29-6jng9.md)
  Returns the weight associated with the behavior specified by subscript syntax.
- [- setObject:forKeyedSubscript:](./setobject_forkeyedsubscript_.md)
  Sets the weight for the behavior specified by subscript syntax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkcompositebehavior/subscript(_:)-6krdg)*