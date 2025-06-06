# arguments

**Framework**: Foundation  
**Kind**: property

The arguments for the expression.

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
var arguments: [NSExpression]? { get }
```

#### Discussion

An expression’s arguments is the array of expressions that will be passed as parameters during invocation of the selector on the operand of a function expression.

Accessing this property raises an exception if it is not applicable to the expression.

## See Also

- [var collection: Any](nsexpression/collection.md)
  The collection of expressions in an aggregate expression, or the collection element of a subquery expression.
- [var constantValue: Any?](nsexpression/constantvalue.md)
  The constant value of the expression.
- [var expressionType: NSExpression.ExpressionType](nsexpression/expressiontype-swift.property.md)
  The expression type for the expression.
- [NSExpression.ExpressionType](nsexpression/expressiontype-swift.enum.md)
  Defines the possible types of an expression.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/arguments)*