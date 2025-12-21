# evaluatePredicate(in:)

**Framework**: GameplayKit  
**Kind**: method

Returns a Boolean value indicating whether the rule has been satisfied in the context of the specified rule system.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func evaluatePredicate(in system: GKRuleSystem) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the rule is satisfied (and its action should be executed); otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

A rule system calls this method when evaluating its rules.

If the rule was created with the [`init(predicate:assertingFact:grade:)`](gkrule/init(predicate:assertingfact:grade:).md) or [`init(predicate:retractingFact:grade:)`](gkrule/init(predicate:retractingfact:grade:).md), calling this method returns the result of testing the predicate against the provided rule system. If the rule was created with the [`init(blockPredicate:action:)`](gkrule/init(blockpredicate:action:).md) method, calling this method calls the predicate block and returns the result. Otherwise, this method always returns [`false`](https://developer.apple.com/documentation/Swift/false)—subclasses should override this method to implement their own predicate tests.

## See Also

- [func performAction(in: GKRuleSystem)](gkrule/performaction(in:).md)
  Performs actions that should result when the rule is satisfied in the context of the specified rule system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrule/evaluatepredicate(in:))*