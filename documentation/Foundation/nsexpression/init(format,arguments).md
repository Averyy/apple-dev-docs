# init(format:arguments:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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

```objc
+ (NSExpression *) expressionWithFormat:(NSString *) expressionFormat arguments:(va_list) argList;
```

#### Return Value

An initialized `NSExpression` object with the specified arguments.

## Parameters

- `expressionFormat`: The expression format.
- `argList`: A list of arguments to be inserted into the `expressionFormat` string. The argument list is terminated by `nil`.

## See Also

### Creating an Expression
- [init(expressionType: NSExpression.ExpressionType)](./init%28expressiontype%29.md)
  Creates the expression with the specified expression type.
- [init(format: String, argumentArray: [Any])](./init%28format,argumentarray%29.md)
  Creates the expression with the specified expression format and array of arguments.
- [convenience init(format: String, any CVarArg...)](./init%28format,_%29.md)
  Creates the expression with the expression format and arguments list you specify.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates an expression by decoding from the coder you specify.
### Related Documentation
- [+ expressionWithFormat:](./expressionwithformat_.md)
  Creates the expression with the specified expression arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/init(format:arguments:))*