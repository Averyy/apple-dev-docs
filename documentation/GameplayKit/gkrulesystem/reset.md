# reset()

**Framework**: GameplayKit  
**Kind**: method

Returns the rule system to its original agenda and clears all facts.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func reset()
```

#### Discussion

Calling this method restarts the evaluation process: the system removes all rules from the current [`agenda`](gkrulesystem/agenda.md) and [`executed`](gkrulesystem/executed.md) lists and empties the [`facts`](gkrulesystem/facts.md) set. (However, the rule’s [`state`](gkrulesystem/state.md) dictionary is left unchanged.) The system then automatically repopulates its agenda according to the [`salience`](gkrule/salience.md) of each rule in the [`rules`](gkrulesystem/rules.md) array.

## See Also

- [func evaluate()](gkrulesystem/evaluate.md)
  Evaluates the rule system, executing the list of rules in its agenda.
- [var agenda: [GKRule]](gkrulesystem/agenda.md)
  The list of rules to be considered when evaluating the system.
- [var executed: [GKRule]](gkrulesystem/executed.md)
  The list of rules whose actions have been performed during evaluation of the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/reset())*