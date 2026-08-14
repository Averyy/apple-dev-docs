# rules

**Framework**: GameplayKit  
**Kind**: property

The list of rules to be executed when evaluating the system.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var rules: [GKRule] { get }
```

#### Discussion

This array holds all rules under consideration by the system—that is, the union of the [`agenda`](gkrulesystem/agenda.md) and [`executed`](gkrulesystem/executed.md) lists. The agenda holds the rules to be considered when evaluating the system, listed in order of their [`salience`](gkrule/salience.md) values (or, for rules with the same salience, the order in which they were added to the system). During evaluation of the rule system, if a rule on the [`agenda`](gkrulesystem/agenda.md) list is satisfied (that is, its predicate returns [`true`](https://developer.apple.com/documentation/swift/true) and it executes its action) the system moves that rule to the [`executed`](gkrulesystem/executed.md) list.

Changing the salience of a rule already in the rule system does not adjust its position in the agenda, but does determine the order of the new agenda when resetting the system.

## See Also

- [func reset()](gkrulesystem/reset.md)
  Returns the rule system to its original agenda and clears all facts.
- [var agenda: [GKRule]](gkrulesystem/agenda.md)
  The list of rules to be considered when evaluating the system.
- [func evaluate()](gkrulesystem/evaluate.md)
  Evaluates the rule system, executing the list of rules in its agenda.
- [var executed: [GKRule]](gkrulesystem/executed.md)
  The list of rules whose actions have been performed during evaluation of the system.
- [func add(GKRule)](gkrulesystem/add(_:)-76jb5.md)
  Adds the specified rule to the system.
- [func add([GKRule])](gkrulesystem/add(_:)-7u5zw.md)
  Adds the specified list of rules to the system.
- [func removeAllRules()](gkrulesystem/removeallrules.md)
  Removes all rules from the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/rules)*