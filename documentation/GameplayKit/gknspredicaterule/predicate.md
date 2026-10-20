# predicate

**Framework**: GameplayKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, retain, readonly) NSPredicate * predicate;
```

#### Discussion

When the rule is evaluated, GameplayKit tests this predicate against the GKRuleSystem object evaluating the rule.

## See Also

### Evaluating a Rule
- [func evaluatePredicate(in: GKRuleSystem) -> Bool](./evaluatepredicate%28in%29.md)
  Returns a Boolean value indicating whether the rule’s predicate has been satisfied in the context of the specified rule system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknspredicaterule/predicate)*