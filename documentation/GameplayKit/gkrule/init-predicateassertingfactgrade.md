# init(predicate:assertingFact:grade:)

**Framework**: GameplayKit  
**Kind**: init

Creates a data-driven rule with the specified predicate, whose action asserts a fact in the rule system evaluating the rule.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(predicate: NSPredicate, assertingFact fact: any NSObjectProtocol, grade: Float)
```

#### Return Value

A new rule object.

#### Discussion

Rules created using this method encode their predicate and action when archived with the [`NSKeyedArchiver`](https://developer.apple.com/documentation/Foundation/NSKeyedArchiver) class. You can use this feature to support saving and loading rules, editing rules in-game, or building tools that separate your gameplay design and game programming tasks.

Rules based on [`NSPredicate`](https://developer.apple.com/documentation/Foundation/NSPredicate) objects typically test information in the [`state`](gkrulesystem/state.md) dictionary of the rule system evaluating the rule. For example, the following code creates a rule you might use to determine whether an enemy character in a game behaves aggressively. (This example presumes the rule system’s state dictionary contains an object for the key `player`, which in turn exposes a numeric value for the key `health`.)

## Parameters

- `fact`: An object representing a fact to assert when the rule’s predicate is satisfied. (For details on facts in rule systems, see the   property in  .)
- `grade`: An amount by which to increase the fact’s membership grade if the rule’s predicate is satisfied.

## See Also

- [convenience init(predicate: NSPredicate, retractingFact: any NSObjectProtocol, grade: Float)](gkrule/init(predicate:retractingfact:grade:).md)
  Creates a data-driven rule with the specified predicate, whose action retracts a fact in the rule system evaluating the rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrule/init(predicate:assertingfact:grade:))*