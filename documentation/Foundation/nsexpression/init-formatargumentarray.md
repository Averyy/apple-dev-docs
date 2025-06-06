# init(format:argumentArray:)

**Framework**: Foundation  
**Kind**: init

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

#### Return Value

An initialized `NSExpression` object with the specified arguments.

## Parameters

- `expressionFormat`: The expression format.
- `arguments`: An array of arguments to be used with the   string.

## See Also

- [init(expressionType: NSExpression.ExpressionType)](nsexpression/init(expressiontype:).md)
  Creates the expression with the specified expression type.
- [init(format: String, arguments: CVaListPointer)](nsexpression/init(format:arguments:).md)
  Creates the expression with the specified expression format and arguments list.
- [convenience init(format: String, any CVarArg...)](nsexpression/init(format:_:).md)
  Creates the expression with the expression format and arguments list you specify.
- [init?(coder: NSCoder)](nsexpression/init(coder:).md)
  Creates an expression by decoding from the coder you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/init(format:argumentarray:))*