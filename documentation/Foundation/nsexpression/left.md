# left

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The left expression of an aggregate expression.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var left: NSExpression { get }
```

```objc
@property (copy, readonly) NSExpression * leftExpression;
```

## Discussion

Accessing this property raises an exception if it is not applicable to the expression.

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
- [NSExpression.ExpressionType](./expressiontype-swift.enum.md)
  Defines the possible types of an expression.
- [var function: String](./function.md)
  The function for the expression.
- [var keyPath: String](./keypath.md)
  The key path for the expression.
- [var operand: NSExpression](./operand.md)
  The operand for the expression.
- [var predicate: NSPredicate](./predicate.md)
  The predicate of a subquery expression.
- [var right: NSExpression](./right.md)
  The right expression of an aggregate expression.
- [var variable: String](./variable.md)
  The variable for the expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/left)*