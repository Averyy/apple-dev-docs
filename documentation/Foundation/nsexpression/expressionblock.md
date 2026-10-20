# expressionBlock

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The block that executes to evaluate the expression.

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
var expressionBlock: (Any?, [NSExpression], NSMutableDictionary?) -> Any { get }
```

```objc
@property (copy, readonly) id (^expressionBlock)(id , NSArray<NSExpression *> *, NSMutableDictionary *);
```

## See Also

### Related Documentation
- [init(block: (Any?, [NSExpression], NSMutableDictionary?) -> Any, arguments: [NSExpression]?)](./init%28block,arguments%29.md)
  Creates an expression object that uses the block for evaluating objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/expressionblock)*