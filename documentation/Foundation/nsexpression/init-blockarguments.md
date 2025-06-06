# init(block:arguments:)

**Framework**: Foundation  
**Kind**: init

Creates an expression object that uses the block for evaluating objects.

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
init(block: @escaping (Any?, [NSExpression], NSMutableDictionary?) -> Any, arguments: [NSExpression]?)
```

#### Return Value

An expression that filters a collection using the specified Block.

## Parameters

- `block`: The Block returns the  .
- `arguments`: See   for a complete list of arguments.

## See Also

- [var expressionBlock: (Any?, [NSExpression], NSMutableDictionary?) -> Any](nsexpression/expressionblock.md)
  The block that executes to evaluate the expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/init(block:arguments:))*