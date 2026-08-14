# evaluate()

**Framework**: GameplayKit  
**Kind**: method

Evaluates the rule system, executing the list of rules in its agenda.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func evaluate()
```

#### Discussion

When you call this method, the system considers each rule in the [`agenda`](gkrulesystem/agenda.md) list in order. The agenda contains rules in the order of their [`salience`](gkrule/salience.md) values, or for rules with the same salience, the order in which they were added to the system.

For each rule, the system evaluates the rule’s predicate by calling its [`evaluatePredicate(in:)`](gkrule/evaluatepredicate(in:).md) method. The rule’s predicate can evaluate the system’s [`state`](gkrulesystem/state.md) dictionary or call the [`GKRuleSystem`](gkrulesystem.md) methods listed in Drawing Conclusions from Facts to examine the set of facts claimed by the system.

If a rule is satisfied (that is, the [`evaluatePredicate(in:)`](gkrule/evaluatepredicate(in:).md) method returns [`true`](https://developer.apple.com/documentation/swift/true)), the system moves that rule from the [`agenda`](gkrulesystem/agenda.md) list to the [`executed`](gkrulesystem/executed.md) list and performs the rule’s action by calling the rule’s [`performAction(in:)`](gkrule/performaction(in:).md) method. The rule’s action can alter the system’s state dictionary or call the [`GKRuleSystem`](gkrulesystem.md) methods listed in Asserting and Retracting Facts to modify the set of facts claimed by the system.

Because other rules might depend on the set of facts, asserting or retracting facts causes the system to reevaluate itself—a single call to the [`evaluate()`](gkrulesystem/evaluate().md) method can cause the system to consider its set of rules several times. After your call this method returns, the [`agenda`](gkrulesystem/agenda.md) list contains only rules whose actions have not been triggered, the [`executed`](gkrulesystem/executed.md) list contains rules that have executed, and the [`state`](gkrulesystem/state.md) dictionary and [`facts`](gkrulesystem/facts.md) array together represent the complete set of conclusions drawn by the rule system.

## See Also

- [var agenda: [GKRule]](gkrulesystem/agenda.md)
  The list of rules to be considered when evaluating the system.
- [var executed: [GKRule]](gkrulesystem/executed.md)
  The list of rules whose actions have been performed during evaluation of the system.
- [func reset()](gkrulesystem/reset.md)
  Returns the rule system to its original agenda and clears all facts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/evaluate())*