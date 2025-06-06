# allowEvaluation()

**Framework**: Foundation  
**Kind**: method

Forces a securely decoded expression to allow evaluation.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func allowEvaluation()
```

#### Discussion

When securely decoding an `NSExpression` object encoded using [`NSSecureCoding`](nssecurecoding.md), evaluation is disabled because it is potentially unsafe to evaluate expressions you get out of an archive.

Before you enable evaluation, you should validate key paths, selectors, etc to ensure no erroneous or malicious code will be executed. Once you’ve preflighted the expression, you can enable the expression for evaluation by calling `allowEvaluation`.

## See Also

- [func expressionValue(with: Any?, context: NSMutableDictionary?) -> Any?](nsexpression/expressionvalue(with:context:).md)
  Evaluates an expression using a specified object and context.
- [var `false`: NSExpression](nsexpression/false.md)
  An expression to evalutate if a conditional expression’s predicate evaluates to false.
- [var `true`: NSExpression](nsexpression/true.md)
  An expression to evalutate if a conditional expression’s predicate evaluates to true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/allowevaluation())*