# true

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

Accessing this property raises an exception if it isn’t applicable to the expression.

## See Also

- [func expressionValue(with: Any?, context: NSMutableDictionary?) -> Any?](nsexpression/expressionvalue(with:context:).md)
  Evaluates an expression using a specified object and context.
- [func allowEvaluation()](nsexpression/allowevaluation.md)
  Forces a securely decoded expression to allow evaluation.
- [var `false`: NSExpression](nsexpression/false.md)
  An expression to evalutate if a conditional expression’s predicate evaluates to false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/true)*