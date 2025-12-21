# evaluatePredicate(in:)

**Framework**: GameplayKit  
**Kind**: method

Returns a Boolean value indicating whether the rule’s predicate has been satisfied in the context of the specified rule system.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func evaluatePredicate(in system: GKRuleSystem) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the rule is satisfied (and its action should be executed); otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

The [`GKNSPredicateRule`](gknspredicaterule.md) class overrides this method to use its [`predicate`](gknspredicaterule/predicate.md) property for testing the rule. Subclasses of [`GKNSPredicateRule`](gknspredicaterule.md) do not need to override this method.

## See Also

- [var predicate: NSPredicate](gknspredicaterule/predicate.md)
  A predicate to be tested when evaluating the rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknspredicaterule/evaluatepredicate(in:))*