# init(expressionType:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates the expression with the specified expression type.

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
init(expressionType type: NSExpression.ExpressionType)
```

```objc
- (instancetype) initWithExpressionType:(NSExpressionType) type;
```

#### Return Value

An initialized `NSExpression` object of the type `type`.

#### Discussion

This method is the designated initializer for `NSExpression`.

## Parameters

- `type`: The type of the new expression, as defined by [`NSExpression.ExpressionType`](./expressiontype-swift.enum.md).

## See Also

### Related Documentation
- [Predicate Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html#//apple_ref/doc/uid/TP40001789)
### Creating an Expression
- [init(format: String, argumentArray: [Any])](./init%28format,argumentarray%29.md)
  Creates the expression with the specified expression format and array of arguments.
- [init(format: String, arguments: CVaListPointer)](./init%28format,arguments%29.md)
  Creates the expression with the specified expression format and arguments list.
- [convenience init(format: String, any CVarArg...)](./init%28format,_%29.md)
  Creates the expression with the expression format and arguments list you specify.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates an expression by decoding from the coder you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/init(expressiontype:))*