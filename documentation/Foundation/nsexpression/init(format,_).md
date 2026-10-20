# init(format:_:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates the expression with the expression format and arguments list you specify.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(format expressionFormat: String, _ args: any CVarArg...)
```

## Parameters

- `expressionFormat`: The expression format.
- `args`: A list of arguments to insert into the `expressionFormat` string.

## See Also

### Creating an Expression
- [init(expressionType: NSExpression.ExpressionType)](./init%28expressiontype%29.md)
  Creates the expression with the specified expression type.
- [init(format: String, argumentArray: [Any])](./init%28format,argumentarray%29.md)
  Creates the expression with the specified expression format and array of arguments.
- [init(format: String, arguments: CVaListPointer)](./init%28format,arguments%29.md)
  Creates the expression with the specified expression format and arguments list.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates an expression by decoding from the coder you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/init(format:_:))*