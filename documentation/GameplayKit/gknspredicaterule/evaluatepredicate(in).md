# evaluatePredicate(in:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) evaluatePredicateWithSystem:(GKRuleSystem *) system;
```

#### Return Value

[`true`](../../Swift/true.md) if the rule is satisfied (and its action should be executed); otherwise, [`false`](../../Swift/false.md).

#### Discussion

The [`GKNSPredicateRule`](../gknspredicaterule.md) class overrides this method to use its [`predicate`](./predicate.md) property for testing the rule. Subclasses of [`GKNSPredicateRule`](../gknspredicaterule.md) do not need to override this method.

## See Also

### Evaluating a Rule
- [var predicate: NSPredicate](./predicate.md)
  A predicate to be tested when evaluating the rule.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknspredicaterule/evaluatepredicate(in:))*