# subscript(_:)

**Framework**: GameplayKit  
**Kind**: subscript  
**Role**: Instance Subscript

Returns the goal at the specified index in the behavior’s list of goals.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
subscript(idx: Int) -> GKGoal { get }
```

```objc
- (GKGoal *) objectAtIndexedSubscript:(NSUInteger) idx;
```

#### Return Value

The goal at the specified index.

#### Discussion

The order of goals in a behavior is undefined. However, you can use this method to enumerate all goals in a behavior.

## Parameters

- `idx`: An index in the behavior’s list of goals; must be less than the value of the [`goalCount`](./goalcount.md) property.

## See Also

### Working with Goals Using Subscript Syntax
- [subscript(GKGoal) -> NSNumber!](./subscript%28_%29-2yvko.md)
  Returns the weight associated with the goal specified by subscript syntax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkbehavior/subscript(_:)-997a9)*