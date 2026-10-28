# expressionWithFormat:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates the expression with the specified expression arguments.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (NSExpression *) expressionWithFormat:(NSString *) expressionFormat;
```

## Return Value

An initialized `NSExpression` object with the specified format.

## Discussion

After `expressionFormat`, pass a comma-separated list of arguments to substitute into format as variadic arguments. The list is terminated by `nil`.

## Parameters

- `expressionFormat`: The expression format.

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/expressionwithformat:)*