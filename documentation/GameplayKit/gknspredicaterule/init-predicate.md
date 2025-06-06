# init(predicate:)

**Framework**: GameplayKit  
**Kind**: init

Initializes a rule with the specified predicate.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(predicate: NSPredicate)
```

#### Return Value

A new predicate-based rule object.

#### Discussion

Rules based on [`NSPredicate`](https://developer.apple.com/documentation/Foundation/NSPredicate) objects typically test information in the [`state`](gkrulesystem/state.md) dictionary of the rule system evaluating the rule. For example, the following code creates a rule you might use to determine whether an enemy character in a game behaves aggressively.

This example presumes the rule system’s state dictionary contains an object for the key `player`, which in turn exposes a numeric value for the key `health`. The [`GKNSPredicateRule`](gknspredicaterule.md) class by itself does nothing in its [`performAction(in:)`](gkrule/performaction(in:).md) method—to create actions for predicate-based rules, you must subclass [`GKNSPredicateRule`](gknspredicaterule.md).

For more information, see [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Parameters

- `predicate`: A predicate to be tested when evaluating the rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknspredicaterule/init(predicate:))*