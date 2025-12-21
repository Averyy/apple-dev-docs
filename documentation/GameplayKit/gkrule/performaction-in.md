# performAction(in:)

**Framework**: GameplayKit  
**Kind**: method

Performs actions that should result when the rule is satisfied in the context of the specified rule system.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func performAction(in system: GKRuleSystem)
```

#### Discussion

A rule system calls this method when evaluating its rules, if and only if the rule’s predicate has been satisfied (that is, the [`evaluatePredicate(in:)`](gkrule/evaluatepredicate(in:).md) method has returned [`true`](https://developer.apple.com/documentation/Swift/true)), and after moving the rule from its [`agenda`](gkrulesystem/agenda.md) list to its [`executed`](gkrulesystem/executed.md) list.

If the rule was created with the [`init(predicate:assertingFact:grade:)`](gkrule/init(predicate:assertingfact:grade:).md) or [`init(predicate:retractingFact:grade:)`](gkrule/init(predicate:retractingfact:grade:).md), calling this method asserts or retracts the fact as specified in the provided rule system. If the rule was created with the [`init(blockPredicate:action:)`](gkrule/init(blockpredicate:action:).md) method, calling this method calls the action block. Otherwise, this method does nothing—subclasses should override this method to implement their own actions.

## See Also

- [func evaluatePredicate(in: GKRuleSystem) -> Bool](gkrule/evaluatepredicate(in:).md)
  Returns a Boolean value indicating whether the rule has been satisfied in the context of the specified rule system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrule/performaction(in:))*