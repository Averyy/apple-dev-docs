# expressionType

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The expression type for the expression.

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
var expressionType: NSExpression.ExpressionType { get }
```

```objc
@property (readonly) NSExpressionType expressionType;
```

#### Discussion

Accessing this property raises an exception if it is not applicable to the expression.

## See Also

### Getting Information About an Expression
- [var arguments: [NSExpression]?](./arguments.md)
  The arguments for the expression.
- [var collection: Any](./collection.md)
  The collection of expressions in an aggregate expression, or the collection element of a subquery expression.
- [var constantValue: Any?](./constantvalue.md)
  The constant value of the expression.
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
- [var left: NSExpression](./left.md)
  The left expression of an aggregate expression.
- [var right: NSExpression](./right.md)
  The right expression of an aggregate expression.
- [var variable: String](./variable.md)
  The variable for the expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/expressiontype-swift.property)*