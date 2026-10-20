# evaluatePredicate(in:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) evaluatePredicateWithSystem:(GKRuleSystem *) system;
```

#### Return Value

[`true`](../../Swift/true.md) if the rule is satisfied (and its action should be executed); otherwise, [`false`](../../Swift/false.md).

#### Discussion

A rule system calls this method when evaluating its rules.

If the rule was created with the [`init(predicate:assertingFact:grade:)`](./init%28predicate,assertingfact,grade%29.md) or [`init(predicate:retractingFact:grade:)`](./init%28predicate,retractingfact,grade%29.md), calling this method returns the result of testing the predicate against the provided rule system. If the rule was created with the [`init(blockPredicate:action:)`](./init%28blockpredicate,action%29.md) method, calling this method calls the predicate block and returns the result. Otherwise, this method always returns [`false`](../../Swift/false.md)—subclasses should override this method to implement their own predicate tests.

## See Also

### Evaluating a Rule
- [func performAction(in: GKRuleSystem)](./performaction%28in%29.md)
  Performs actions that should result when the rule is satisfied in the context of the specified rule system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrule/evaluatepredicate(in:))*