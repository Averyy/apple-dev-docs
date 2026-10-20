# NSExpression.ExpressionType

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NSExpressionType : NSUInteger;
```

## Topics

### Constants
- [NSExpression.ExpressionType.constantValue](./expressiontype-swift.enum/constantvalue.md)
  An expression that always returns the same value.
- [NSExpression.ExpressionType.evaluatedObject](./expressiontype-swift.enum/evaluatedobject.md)
  An expression that always returns the parameter object itself.
- [NSExpression.ExpressionType.variable](./expressiontype-swift.enum/variable.md)
  An expression that always returns whatever value is associated with the key specified by ‘variable’ in the bindings dictionary.
- [NSExpression.ExpressionType.keyPath](./expressiontype-swift.enum/keypath.md)
  An expression that returns something that can be used as a key path.
- [NSExpression.ExpressionType.function](./expressiontype-swift.enum/function.md)
  An expression that returns the result of evaluating a function.
- [NSExpression.ExpressionType.unionSet](./expressiontype-swift.enum/unionset.md)
  An expression that creates a union of the results of two nested expressions.
- [NSExpression.ExpressionType.intersectSet](./expressiontype-swift.enum/intersectset.md)
  An expression that creates an intersection of the results of two nested expressions.
- [NSExpression.ExpressionType.minusSet](./expressiontype-swift.enum/minusset.md)
  An expression that combines two nested expression results by set subtraction.
- [NSExpression.ExpressionType.subquery](./expressiontype-swift.enum/subquery.md)
  An expression that filters a collection using a subpredicate.
- [NSExpression.ExpressionType.aggregate](./expressiontype-swift.enum/aggregate.md)
  An expression that defines an aggregate of `NSExpression` objects.
- [NSExpression.ExpressionType.anyKey](./expressiontype-swift.enum/anykey.md)
  An expression that represents any key.
- [NSExpression.ExpressionType.block](./expressiontype-swift.enum/block.md)
  An expression that uses a Block.
- [NSExpression.ExpressionType.conditional](./expressiontype-swift.enum/conditional.md)
  A conditional expression that evaluates a predicate to determine which expression to return.
### Initializers
- [init?(rawValue: UInt)](./expressiontype-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting Information About an Expression
- [var arguments: [NSExpression]?](./arguments.md)
  The arguments for the expression.
- [var collection: Any](./collection.md)
  The collection of expressions in an aggregate expression, or the collection element of a subquery expression.
- [var constantValue: Any?](./constantvalue.md)
  The constant value of the expression.
- [var expressionType: NSExpression.ExpressionType](./expressiontype-swift.property.md)
  The expression type for the expression.
- [var function: String](./function.md)
  The function for the expression.
- [var keyPath: String](./keypath.md)
  The key path for the expression.
- [var operand: NSExpression](./operand.md)
  The operand for the expression.
- [var predicate: NSPredicate](./predicate.md)
  The predicate of a subquery expression.
- [var left: NSExpression](./left.md)
  The left expression of an aggregate expression.
- [var right: NSExpression](./right.md)
  The right expression of an aggregate expression.
- [var variable: String](./variable.md)
  The variable for the expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/expressiontype-swift.enum)*