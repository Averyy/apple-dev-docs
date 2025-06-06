# assertFact(_:)

**Framework**: GameplayKit  
**Kind**: method

Adds the specified fact to the fact set with a membership grade of 1.0, and reevaluates the rules in the system’s agenda.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func assertFact(_ fact: any NSObjectProtocol)
```

#### Discussion

Calling this method is equivalent to calling the [`assertFact(_:grade:)`](gkrulesystem/assertfact(_:grade:).md) method with a `grade` value of 1.0. Asserting a fact adds it to the [`facts`](gkrulesystem/facts.md) array if it is not already present.

Upon asserting or retracting any facts, the system reevaluates the rules in its [`agenda`](gkrulesystem/agenda.md) list so any rules that depend on changes to the set of facts can perform their actions.

## Parameters

- `fact`: An object representing a truth to be claimed by the rule system. For details, see the   property.

## See Also

- [var facts: [Any]](gkrulesystem/facts.md)
  The list of facts claimed by the rule system.
- [func assertFact(any NSObjectProtocol, grade: Float)](gkrulesystem/assertfact(_:grade:).md)
  Increases the membership grade of the specified fact by the specified amount, adding it to the fact set if necessary, and reevaluates the rules in the system’s agenda.
- [func retractFact(any NSObjectProtocol)](gkrulesystem/retractfact(_:).md)
  Removes the specified fact from the fact set, and reevaluates the rules in the system’s agenda.
- [func retractFact(any NSObjectProtocol, grade: Float)](gkrulesystem/retractfact(_:grade:).md)
  Reduces the membership grade of the specified fact by the specified amount, removing it from the fact set if necessary, and reevaluates the rules in the system’s agenda.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/assertfact(_:))*