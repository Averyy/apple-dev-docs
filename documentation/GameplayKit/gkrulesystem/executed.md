# executed

**Framework**: GameplayKit  
**Kind**: property

The list of rules whose actions have been performed during evaluation of the system.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var executed: [GKRule] { get }
```

#### Discussion

When you call the [`evaluate()`](gkrulesystem/evaluate().md) method, the system considers each rule in the [`agenda`](gkrulesystem/agenda.md) list in order. If a rule on the agenda is satisfied—that is, its predicate returns [`true`](https://developer.apple.com/documentation/Swift/true) and it executes its action—the system moves that rule to the [`executed`](gkrulesystem/executed.md) list.

## See Also

- [var rules: [GKRule]](gkrulesystem/rules.md)
  The list of rules to be executed when evaluating the system.
- [func evaluate()](gkrulesystem/evaluate.md)
  Evaluates the rule system, executing the list of rules in its agenda.
- [var agenda: [GKRule]](gkrulesystem/agenda.md)
  The list of rules to be considered when evaluating the system.
- [func reset()](gkrulesystem/reset.md)
  Returns the rule system to its original agenda and clears all facts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/executed)*