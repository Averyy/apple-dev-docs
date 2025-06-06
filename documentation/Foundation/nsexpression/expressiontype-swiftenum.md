# NSExpression.ExpressionType

**Framework**: Foundation  
**Kind**: enum

Defines the possible types of an expression.

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
enum ExpressionType
```

## Topics

### Constants
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
- [NSExpression.ExpressionType.block](nsexpression/expressiontype-swift.enum/block.md)
  An expression that uses a Block.
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
- [NSExpression.ExpressionType.block](nsexpression/expressiontype-swift.enum/block.md)
  An expression that uses a Block.
### Enumeration Cases
- [NSExpression.ExpressionType.conditional](nsexpression/expressiontype-swift.enum/conditional.md)
- [NSExpression.ExpressionType.conditional](nsexpression/expressiontype-swift.enum/conditional.md)
### Initializers
- [init?(rawValue: UInt)](nsexpression/expressiontype-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var arguments: [NSExpression]?](nsexpression/arguments.md)
  The arguments for the expression.
- [var collection: Any](nsexpression/collection.md)
  The collection of expressions in an aggregate expression, or the collection element of a subquery expression.
- [var constantValue: Any?](nsexpression/constantvalue.md)
  The constant value of the expression.
- [var expressionType: NSExpression.ExpressionType](nsexpression/expressiontype-swift.property.md)
  The expression type for the expression.
- [var function: String](nsexpression/function.md)
  The function for the expression.
- [var keyPath: String](nsexpression/keypath.md)
  The key path for the expression.
- [var operand: NSExpression](nsexpression/operand.md)
  The operand for the expression.
- [var predicate: NSPredicate](nsexpression/predicate.md)
  The predicate of a subquery expression.
- [var left: NSExpression](nsexpression/left.md)
  The left expression of an aggregate expression.
- [var right: NSExpression](nsexpression/right.md)
  The right expression of an aggregate expression.
- [var variable: String](nsexpression/variable.md)
  The variable for the expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/expressiontype-swift.enum)*