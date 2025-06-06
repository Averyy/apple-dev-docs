# state

**Framework**: GameplayKit  
**Kind**: property

A dictionary of state information to be evaluated by the system’s rules.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var state: NSMutableDictionary { get }
```

#### Discussion

This dictionary is mutable—some rules might alter the system’s state when executed. If you change this dictionary’s contents outside of a rule action, you must reset and reevaluate the system.

## See Also

- [func reset()](gkrulesystem/reset.md)
  Returns the rule system to its original agenda and clears all facts.
- [func evaluate()](gkrulesystem/evaluate.md)
  Evaluates the rule system, executing the list of rules in its agenda.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/state)*