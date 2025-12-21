# agenda

**Framework**: GameplayKit  
**Kind**: property

The list of rules to be considered when evaluating the system.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var agenda: [GKRule] { get }
```

#### Discussion

The agenda holds the rules to be considered when evaluating the system, listed in order of their [`salience`](gkrule/salience.md) values (or, for rules with the same salience, the order in which they were added to the system). During evaluation of the rule system, if a rule on the [`agenda`](gkrulesystem/agenda.md) list is satisfied—that is, its predicate returns [`true`](https://developer.apple.com/documentation/Swift/true) and it executes its action—the system moves that rule to the [`executed`](gkrulesystem/executed.md) list.

Changing the salience of a rule already in the rule system does not adjust its position in the agenda, but does determine the order of the new agenda when resetting the system.

## See Also

- [var rules: [GKRule]](gkrulesystem/rules.md)
  The list of rules to be executed when evaluating the system.
- [func evaluate()](gkrulesystem/evaluate.md)
  Evaluates the rule system, executing the list of rules in its agenda.
- [var executed: [GKRule]](gkrulesystem/executed.md)
  The list of rules whose actions have been performed during evaluation of the system.
- [func reset()](gkrulesystem/reset.md)
  Returns the rule system to its original agenda and clears all facts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/agenda)*