# init(coder:)

**Framework**: Foundation  
**Kind**: init

Creates an expression by decoding from the coder you specify.

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
init?(coder: NSCoder)
```

## Parameters

- `coder`: The coder to read data from.

## See Also

- [init(expressionType: NSExpression.ExpressionType)](nsexpression/init(expressiontype:).md)
  Creates the expression with the specified expression type.
- [init(format: String, argumentArray: [Any])](nsexpression/init(format:argumentarray:).md)
  Creates the expression with the specified expression format and array of arguments.
- [init(format: String, arguments: CVaListPointer)](nsexpression/init(format:arguments:).md)
  Creates the expression with the specified expression format and arguments list.
- [convenience init(format: String, any CVarArg...)](nsexpression/init(format:_:).md)
  Creates the expression with the expression format and arguments list you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/init(coder:))*