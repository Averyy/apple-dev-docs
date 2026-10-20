# performAction(in:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) performActionWithSystem:(GKRuleSystem *) system;
```

#### Discussion

A rule system calls this method when evaluating its rules, if and only if the rule’s predicate has been satisfied (that is, the [`evaluatePredicate(in:)`](./evaluatepredicate%28in%29.md) method has returned [`true`](../../Swift/true.md)), and after moving the rule from its [`agenda`](../gkrulesystem/agenda.md) list to its [`executed`](../gkrulesystem/executed.md) list.

If the rule was created with the [`init(predicate:assertingFact:grade:)`](./init%28predicate,assertingfact,grade%29.md) or [`init(predicate:retractingFact:grade:)`](./init%28predicate,retractingfact,grade%29.md), calling this method asserts or retracts the fact as specified in the provided rule system. If the rule was created with the [`init(blockPredicate:action:)`](./init%28blockpredicate,action%29.md) method, calling this method calls the action block. Otherwise, this method does nothing—subclasses should override this method to implement their own actions.

## See Also

### Evaluating a Rule
- [func evaluatePredicate(in: GKRuleSystem) -> Bool](./evaluatepredicate%28in%29.md)
  Returns a Boolean value indicating whether the rule has been satisfied in the context of the specified rule system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrule/performaction(in:))*