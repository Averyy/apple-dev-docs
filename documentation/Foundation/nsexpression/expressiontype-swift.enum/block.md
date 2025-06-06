# NSExpression.ExpressionType.block

**Framework**: Foundation  
**Kind**: case

An expression that uses a Block.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case block
```

## See Also

- [NSExpression.ExpressionType.constantValue](nsexpression/expressiontype-swift.enum/constantvalue.md)
  An expression that always returns the same value.
- [NSExpression.ExpressionType.evaluatedObject](nsexpression/expressiontype-swift.enum/evaluatedobject.md)
  An expression that always returns the parameter object itself.
- [NSExpression.ExpressionType.variable](nsexpression/expressiontype-swift.enum/variable.md)
  An expression that always returns whatever value is associated with the key specified by ‘variable’ in the bindings dictionary.
- [NSExpression.ExpressionType.keyPath](nsexpression/expressiontype-swift.enum/keypath.md)
  An expression that returns something that can be used as a key path.
- [NSExpression.ExpressionType.function](nsexpression/expressiontype-swift.enum/function.md)
  An expression that returns the result of evaluating a function.
- [NSExpression.ExpressionType.unionSet](nsexpression/expressiontype-swift.enum/unionset.md)
  An expression that creates a union of the results of two nested expressions.
- [NSExpression.ExpressionType.intersectSet](nsexpression/expressiontype-swift.enum/intersectset.md)
  An expression that creates an intersection of the results of two nested expressions.
- [NSExpression.ExpressionType.minusSet](nsexpression/expressiontype-swift.enum/minusset.md)
  An expression that combines two nested expression results by set subtraction.
- [NSExpression.ExpressionType.subquery](nsexpression/expressiontype-swift.enum/subquery.md)
  An expression that filters a collection using a subpredicate.
- [NSExpression.ExpressionType.aggregate](nsexpression/expressiontype-swift.enum/aggregate.md)
  An expression that defines an aggregate of `NSExpression` objects.
- [NSExpression.ExpressionType.anyKey](nsexpression/expressiontype-swift.enum/anykey.md)
  An expression that represents any key.
- [NSExpression.ExpressionType.constantValue](nsexpression/expressiontype-swift.enum/constantvalue.md)
  An expression that always returns the same value.
- [NSExpression.ExpressionType.evaluatedObject](nsexpression/expressiontype-swift.enum/evaluatedobject.md)
  An expression that always returns the parameter object itself.
- [NSExpression.ExpressionType.variable](nsexpression/expressiontype-swift.enum/variable.md)
  An expression that always returns whatever value is associated with the key specified by ‘variable’ in the bindings dictionary.
- [NSExpression.ExpressionType.keyPath](nsexpression/expressiontype-swift.enum/keypath.md)
  An expression that returns something that can be used as a key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/expressiontype-swift.enum/block)*