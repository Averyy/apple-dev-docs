# init(forConditional:trueExpression:falseExpression:)

**Framework**: Foundation  
**Kind**: init

Creates an expression that returns a result, depending on the value of predicate.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(forConditional predicate: NSPredicate, trueExpression: NSExpression, falseExpression: NSExpression)
```

## Parameters

- `predicate`: The predicate for determining whether the element belongs in the result collection.
- `trueExpression`: The expression for evaluation when the predicate evaluates to  .
- `falseExpression`: The expression for evaluation when the predicate evaluates to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/init(forconditional:trueexpression:falseexpression:))*