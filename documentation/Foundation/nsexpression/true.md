# true

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

An expression to evalutate if a conditional expression’s predicate evaluates to true.

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
@NSCopying
var `true`: NSExpression { get }
```

```objc
@property (copy, readonly) NSExpression * trueExpression;
```

## Discussion

Accessing this property raises an exception if it isn’t applicable to the expression.

## See Also

### Evaluating an Expression
- [func expressionValue(with: Any?, context: NSMutableDictionary?) -> Any?](./expressionvalue%28with,context%29.md)
  Evaluates an expression using a specified object and context.
- [func allowEvaluation()](./allowevaluation%28%29.md)
  Forces a securely decoded expression to allow evaluation.
- [var `false`: NSExpression](./false.md)
  An expression to evalutate if a conditional expression’s predicate evaluates to false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/true)*