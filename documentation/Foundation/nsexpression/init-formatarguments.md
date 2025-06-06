# init(format:arguments:)

**Framework**: Foundation  
**Kind**: init

Creates the expression with the specified expression format and arguments list.

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
init(format expressionFormat: String, arguments argList: CVaListPointer)
```

#### Return Value

An initialized `NSExpression` object with the specified arguments.

## Parameters

- `expressionFormat`: The expression format.
- `argList`: A list of arguments to be inserted into the   string. The argument list is terminated by  .

## See Also

- [init(expressionType: NSExpression.ExpressionType)](nsexpression/init(expressiontype:).md)
  Creates the expression with the specified expression type.
- [init(format: String, argumentArray: [Any])](nsexpression/init(format:argumentarray:).md)
  Creates the expression with the specified expression format and array of arguments.
- [convenience init(format: String, any CVarArg...)](nsexpression/init(format:_:).md)
  Creates the expression with the expression format and arguments list you specify.
- [init?(coder: NSCoder)](nsexpression/init(coder:).md)
  Creates an expression by decoding from the coder you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/init(format:arguments:))*