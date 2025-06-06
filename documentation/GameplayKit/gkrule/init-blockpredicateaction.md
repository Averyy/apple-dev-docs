# init(blockPredicate:action:)

**Framework**: GameplayKit  
**Kind**: init

Creates a rule whose predicate is evaluated and action is executed through the specified blocks.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(blockPredicate predicate: @escaping (GKRuleSystem) -> Bool, action: @escaping (GKRuleSystem) -> Void)
```

#### Return Value

A new rule object.

#### Discussion

Rules created using this method can run arbitrary code in their predicate and action, but do not encode their predicate or action when archiving with the [`NSKeyedArchiver`](https://developer.apple.com/documentation/Foundation/NSKeyedArchiver) class. For archivable rules, use the [`GKRule`](gkrule.md) methods listed in Creating Data-Driven Rules.

## Parameters

- `action`: A block to be invoked after the rule’s predicate is satisfied. The block takes a single parameter:


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrule/init(blockpredicate:action:))*