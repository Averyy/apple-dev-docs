# expressionValue(with:context:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Evaluates an expression using a specified object and context.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func expressionValue(with object: Any?, context: NSMutableDictionary?) -> Any?
```

```objc
- (id) expressionValueWithObject:(id) object context:(NSMutableDictionary *) context;
```

## Return Value

The evaluated object.

## Parameters

- `object`: The object against which the expression is evaluated.
- `context`: A dictionary that the expression can use to store temporary state for one predicate evaluation. Can be `nil`.

  Note that `context` is mutable, and that it can only be accessed during the evaluation of the expression. You must not attempt to retain it for use elsewhere.

## See Also

### Evaluating an Expression
- [func allowEvaluation()](./allowevaluation%28%29.md)
  Forces a securely decoded expression to allow evaluation.
- [var `false`: NSExpression](./false.md)
  An expression to evalutate if a conditional expression’s predicate evaluates to false.
- [var `true`: NSExpression](./true.md)
  An expression to evalutate if a conditional expression’s predicate evaluates to true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/expressionvalue(with:context:))*