# GKRule

**Framework**: GameplayKit  
**Kind**: class

A rule to be used in the context of a rule system, with a predicate to be tested and an action to be executed when the test succeeds.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKRule
```

#### Overview

Evaluating a [`GKRuleSystem`](gkrulesystem.md) object tests each of its rules, which typically examine the state or facts associated with the rule system, and executes the actions specified by each rule whose test passes, such as asserting or retracting facts in the rule system or modifying its state.

A rule has two parts: a predicate and an action.

- The rule’s  determines whether the rule has been satisfied, within the context of a given rule system. Evaluating a rule’s predicate typically involves examining information in the rule sytem’s [`state`](gkrulesystem/state.md) dictionary or testing the membership grade of facts claimed by the system (see the [`facts`](gkrulesystem/facts.md) property in [`GKRuleSystem`](gkrulesystem.md) for details).
- The rule’s  is executed if and only if the rule’s predicate is satisfied. Rule actions typically involve asserting or retracting facts in the system (see the [`GKRuleSystem`](gkrulesystem.md) methods listed in Asserting and Retracting Facts) or modifying information in the system’s [`state`](gkrulesystem/state.md) dictionary.

There are multiple ways to create rules for use in a rule system, each with its own advantages.

- Typical rule predicates involve conditional logic tests on the properties of the containing rule system, and typical rule actions assert or retract facts. If your rules fit this pattern, you can use the [`init(predicate:assertingFact:grade:)`](gkrule/init(predicate:assertingfact:grade:).md) and [`init(predicate:retractingFact:grade:)`](gkrule/init(predicate:retractingfact:grade:).md) methods to create rules that are entirely data-driven—that is, they can be easily archived for later reuse, edited without compiling source code, and created at runtime.
- To create rules with entirely custom logic for both predicate and action, use the [`init(blockPredicate:action:)`](gkrule/init(blockpredicate:action:).md) method. This method creates rules that are very flexible, but that cannot be archived for reuse.
- To create rules with more complex custom logic, implement your own rule classes: subclass [`GKRule`](gkrule.md) to build custom logic for both the rule’s predicate and its action, or subclass [`GKNSPredicateRule`](gknspredicaterule.md) to use an [`NSPredicate`](https://developer.apple.com/documentation/Foundation/NSPredicate) object for the rule’s predicate and build custom logic only for the rule’s action. The reusability of custom rule classes depends on your implementation of such classes.

For more information about rules and rule systems, read [`Rule Systems`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/RuleSystems.html#//apple_ref/doc/uid/TP40015172-CH10) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

##### Subclassing Notes

GameplayKit evaluates rules in the context of a [`GKRuleSystem`](gkrulesystem.md) object, so custom rule classes should be —that is, they generally should not carry independent state that affects their predicate or action.

###### Methods to Override

Subclasses of [`GKRule`](gkrule.md) must implement both of the following methods:

- Override the [`evaluatePredicate(in:)`](gkrule/evaluatepredicate(in:).md) method to evaluate your rule in the context of the provided rule system.
- Override the [`performAction(in:)`](gkrule/performaction(in:).md) method to perform whatever actions should result when your rule is satisfied (that is, when your [`evaluatePredicate(in:)`](gkrule/evaluatepredicate(in:).md) implementation returns [`true`](https://developer.apple.com/documentation/swift/true)) in the context of the provided rule system.

###### Alternatives to Subclassing

- Use the [`init(predicate:assertingFact:grade:)`](gkrule/init(predicate:assertingfact:grade:).md) or [`init(predicate:retractingFact:grade:)`](gkrule/init(predicate:retractingfact:grade:).md) to create a rule that uses an [`NSPredicate`](https://developer.apple.com/documentation/Foundation/NSPredicate) object for evaluation and whose action asserts or retracts a fact in the containing rule system.
- Subclass [`GKNSPredicateRule`](gknspredicaterule.md) instead to use an [`NSPredicate`](https://developer.apple.com/documentation/Foundation/NSPredicate) object for evaluating the rule and write custom logic only for the rule’s action.
- Use the [`init(blockPredicate:action:)`](gkrule/init(blockpredicate:action:).md) method to quickly create a rule whose custom logic is contained in block objects.

## Topics

### Creating Data-Driven Rules
- [convenience init(predicate: NSPredicate, assertingFact: any NSObjectProtocol, grade: Float)](gkrule/init(predicate:assertingfact:grade:).md)
  Creates a data-driven rule with the specified predicate, whose action asserts a fact in the rule system evaluating the rule.
- [convenience init(predicate: NSPredicate, retractingFact: any NSObjectProtocol, grade: Float)](gkrule/init(predicate:retractingfact:grade:).md)
  Creates a data-driven rule with the specified predicate, whose action retracts a fact in the rule system evaluating the rule.
### Creating Block-Based Rules
- [convenience init(blockPredicate: (GKRuleSystem) -> Bool, action: (GKRuleSystem) -> Void)](gkrule/init(blockpredicate:action:).md)
  Creates a rule whose predicate is evaluated and action is executed through the specified blocks.
### Setting the Order of Rules in a Rule System
- [var salience: Int](gkrule/salience.md)
  The importance of the rule relative to others in a rule system’s agenda.
### Evaluating a Rule
- [func evaluatePredicate(in: GKRuleSystem) -> Bool](gkrule/evaluatepredicate(in:).md)
  Returns a Boolean value indicating whether the rule has been satisfied in the context of the specified rule system.
- [func performAction(in: GKRuleSystem)](gkrule/performaction(in:).md)
  Performs actions that should result when the rule is satisfied in the context of the specified rule system.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [GKNSPredicateRule](gknspredicaterule.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GKNSPredicateRule](gknspredicaterule.md)
  A rule for use in a rule system that uses a Foundation [`NSPredicate`](https://developer.apple.com/documentation/Foundation/NSPredicate) object to evaluate itself.
- [class GKRuleSystem](gkrulesystem.md)
  A list of rules, together with a context for evaluating them and interpreting results, for use in constructing data-driven logic or fuzzy logic systems.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrule)*