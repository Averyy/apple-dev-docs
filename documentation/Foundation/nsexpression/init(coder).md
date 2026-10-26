# init(coder:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## Parameters

- `coder`: The coder to read data from.

## See Also

### Creating an Expression
- [init(expressionType: NSExpression.ExpressionType)](./init%28expressiontype%29.md)
  Creates the expression with the specified expression type.
- [init(format: String, argumentArray: [Any])](./init%28format,argumentarray%29.md)
  Creates the expression with the specified expression format and array of arguments.
- [init(format: String, arguments: CVaListPointer)](./init%28format,arguments%29.md)
  Creates the expression with the specified expression format and arguments list.
- [convenience init(format: String, any CVarArg...)](./init%28format,_%29.md)
  Creates the expression with the expression format and arguments list you specify.
- [+ expressionWithFormat:](./expressionwithformat_.md)
  Creates the expression with the specified expression arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/init(coder:))*