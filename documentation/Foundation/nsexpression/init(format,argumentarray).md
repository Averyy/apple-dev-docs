# init(format:argumentArray:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates the expression with the specified expression format and array of arguments.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(format expressionFormat: String, argumentArray arguments: [Any])
```

```objc
+ (NSExpression *) expressionWithFormat:(NSString *) expressionFormat argumentArray:(NSArray *) arguments;
```

#### Return Value

An initialized `NSExpression` object with the specified arguments.

## Parameters

- `expressionFormat`: The expression format.
- `arguments`: An array of arguments to be used with the `expressionFormat` string.

## See Also

### Creating an Expression
- [init(expressionType: NSExpression.ExpressionType)](./init%28expressiontype%29.md)
  Creates the expression with the specified expression type.
- [init(format: String, arguments: CVaListPointer)](./init%28format,arguments%29.md)
  Creates the expression with the specified expression format and arguments list.
- [convenience init(format: String, any CVarArg...)](./init%28format,_%29.md)
  Creates the expression with the expression format and arguments list you specify.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates an expression by decoding from the coder you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/init(format:argumentarray:))*