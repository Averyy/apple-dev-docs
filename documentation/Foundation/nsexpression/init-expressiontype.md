# init(expressionType:)

**Framework**: Foundation  
**Kind**: init

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

#### Return Value

An initialized `NSExpression` object of the type `type`.

#### Discussion

This method is the designated initializer for `NSExpression`.

## Parameters

- `type`: The type of the new expression, as defined by  .

## See Also

- [Predicate Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html#//apple_ref/doc/uid/TP40001789)
- [init(format: String, argumentArray: [Any])](nsexpression/init(format:argumentarray:).md)
  Creates the expression with the specified expression format and array of arguments.
- [init(format: String, arguments: CVaListPointer)](nsexpression/init(format:arguments:).md)
  Creates the expression with the specified expression format and arguments list.
- [convenience init(format: String, any CVarArg...)](nsexpression/init(format:_:).md)
  Creates the expression with the expression format and arguments list you specify.
- [init?(coder: NSCoder)](nsexpression/init(coder:).md)
  Creates an expression by decoding from the coder you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/init(expressiontype:))*