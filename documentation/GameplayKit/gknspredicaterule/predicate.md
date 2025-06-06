# predicate

**Framework**: GameplayKit  
**Kind**: property

A predicate to be tested when evaluating the rule.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var predicate: NSPredicate { get }
```

#### Discussion

When the rule is evaluated, GameplayKit tests this predicate against the GKRuleSystem object evaluating the rule.

## See Also

- [func evaluatePredicate(in: GKRuleSystem) -> Bool](gknspredicaterule/evaluatepredicate(in:).md)
  Returns a Boolean value indicating whether the rule’s predicate has been satisfied in the context of the specified rule system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknspredicaterule/predicate)*