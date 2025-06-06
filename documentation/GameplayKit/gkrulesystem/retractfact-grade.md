# retractFact(_:grade:)

**Framework**: GameplayKit  
**Kind**: method

Reduces the membership grade of the specified fact by the specified amount, removing it from the fact set if necessary, and reevaluates the rules in the system’s agenda.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func retractFact(_ fact: any NSObjectProtocol, grade: Float)
```

#### Discussion

Each fact has a membership grade ranging from zero to 1.0, representing variable levels of truth, strength, or confidence for use in fuzzy logic. Calling this method reduces the fact’s grade by the amount specified in the `grade` parameter; reducing a fact’s grade to zero or below removes it from the [`facts`](gkrulesystem/facts.md) array.

Upon asserting or retracting any facts, the system reevaluates the rules in its [`agenda`](gkrulesystem/agenda.md) list so any rules that depend on changes to the set of facts can perform their actions.

## Parameters

- `fact`: An object representing a truth to be claimed or rejected by the rule system. For details, see the   property.
- `grade`: The amount by which to reduce the fact’s membership grade.

## See Also

- [var facts: [Any]](gkrulesystem/facts.md)
  The list of facts claimed by the rule system.
- [func assertFact(any NSObjectProtocol)](gkrulesystem/assertfact(_:).md)
  Adds the specified fact to the fact set with a membership grade of 1.0, and reevaluates the rules in the system’s agenda.
- [func assertFact(any NSObjectProtocol, grade: Float)](gkrulesystem/assertfact(_:grade:).md)
  Increases the membership grade of the specified fact by the specified amount, adding it to the fact set if necessary, and reevaluates the rules in the system’s agenda.
- [func retractFact(any NSObjectProtocol)](gkrulesystem/retractfact(_:).md)
  Removes the specified fact from the fact set, and reevaluates the rules in the system’s agenda.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/retractfact(_:grade:))*