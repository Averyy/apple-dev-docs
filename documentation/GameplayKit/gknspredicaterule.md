# GKNSPredicateRule

**Framework**: GameplayKit  
**Kind**: class

A rule for use in a rule system that uses a Foundation [`NSPredicate`](https://developer.apple.com/documentation/Foundation/NSPredicate) object to evaluate itself.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKNSPredicateRule
```

#### Overview

The [`GKNSPredicateRule`](gknspredicaterule.md) class is a specialized subclass of the [`GKRule`](gkrule.md) class (which represents rules to be used by [`GKRuleSystem`](gkrulesystem.md) objects). Custom subclasses of [`GKNSPredicateRule`](gknspredicaterule.md) use an [`NSPredicate`](https://developer.apple.com/documentation/Foundation/NSPredicate) object to evaluate a rule, rather than requiring custom logic for evaluation as is the case with custom [`GKRule`](gkrule.md) subclasses.

For more information about rules and rule systems, read [`Rule Systems`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/RuleSystems.html#//apple_ref/doc/uid/TP40015172-CH10) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

##### Subclassing Notes

GameplayKit evaluates rules in the context of a [`GKRuleSystem`](gkrulesystem.md) object, so custom rule classes should be —that is, they generally should not carry independent state that affects their predicate or action.

###### Methods to Override

Override the [`performAction(in:)`](gkrule/performaction(in:).md) method to perform whatever actions should result when your rule is satisfied (that is, when its [`predicate`](gknspredicaterule/predicate.md) property evaluates to true in the context of the provided rule system).

###### Alternatives to Subclassing

- Use the [`GKRule`](gkrule.md) method [`init(predicate:assertingFact:grade:)`](gkrule/init(predicate:assertingfact:grade:).md) or [`init(predicate:retractingFact:grade:)`](gkrule/init(predicate:retractingfact:grade:).md) to create a rule that uses an [`NSPredicate`](https://developer.apple.com/documentation/Foundation/NSPredicate) object for evaluation and whose action asserts or retracts a fact in the containing rule system.
- Use the [`GKRule`](gkrule.md) method [`init(blockPredicate:action:)`](gkrule/init(blockpredicate:action:).md) method to quickly create a rule whose custom logic is contained in block objects.

## Topics

### Creating a Predicate-Based Rule
- [init(predicate: NSPredicate)](gknspredicaterule/init(predicate:).md)
  Initializes a rule with the specified predicate.
### Evaluating a Rule
- [var predicate: NSPredicate](gknspredicaterule/predicate.md)
  A predicate to be tested when evaluating the rule.
- [func evaluatePredicate(in: GKRuleSystem) -> Bool](gknspredicaterule/evaluatepredicate(in:).md)
  Returns a Boolean value indicating whether the rule’s predicate has been satisfied in the context of the specified rule system.

## Relationships

### Inherits From
- [GKRule](gkrule.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GKRule](gkrule.md)
  A rule to be used in the context of a rule system, with a predicate to be tested and an action to be executed when the test succeeds.
- [class GKRuleSystem](gkrulesystem.md)
  A list of rules, together with a context for evaluating them and interpreting results, for use in constructing data-driven logic or fuzzy logic systems.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gknspredicaterule)*