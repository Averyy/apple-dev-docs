# minimumGrade(forFacts:)

**Framework**: Gameplaykit  
**Kind**: method

Returns the lowest membership grade among the specified facts.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func minimumGrade(forFacts facts: [Any]) -> Float
```

#### Return Value

The lowest membership grade in the array of facts.

#### Discussion

In fuzzy logic, this method is called the AND Zadeh operator, because it corresponds to the AND operator in Boolean logic.

> **Note**:  If a fact is not in the [`facts`](gkrulesystem/facts.md) array, its membership grade for purposes of this operation is implicitly zero.

## Parameters

- `facts`: An array of objects representing truths claimed or rejected by the rule system. For details, see the   property.

## See Also

- [var facts: [Any]](gkrulesystem/facts.md)
  The list of facts claimed by the rule system.
- [func grade(forFact: any NSObjectProtocol) -> Float](gkrulesystem/grade(forfact:).md)
  Returns the membership grade of the specified fact.
- [func maximumGrade(forFacts: [Any]) -> Float](gkrulesystem/maximumgrade(forfacts:).md)
  Returns the highest membership grade among the specified facts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/minimumgrade(forfacts:))*