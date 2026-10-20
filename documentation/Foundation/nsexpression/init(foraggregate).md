# init(forAggregate:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates an aggregate expression for a specified collection.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(forAggregate subexpressions: [NSExpression])
```

```objc
+ (NSExpression *) expressionForAggregate:(NSArray<NSExpression *> *) subexpressions;
```

#### Return Value

A new expression that contains the expressions in `collection`.

## Parameters

- `subexpressions`: A collection object (an instance of `NSArray`, `NSSet`, or `NSDictionary`) that contains further expressions.

## See Also

### Creating a Collection Expression
- [init(forUnionSet: NSExpression, with: NSExpression)](./init%28forunionset,with%29.md)
  Creates an expression object that represents the union of a specified set and collection.
- [init(forIntersectSet: NSExpression, with: NSExpression)](./init%28forintersectset,with%29.md)
  Creates an expression object that represents the intersection of a specified set and collection.
- [init(forMinusSet: NSExpression, with: NSExpression)](./init%28forminusset,with%29.md)
  Creates an expression object that represents the subtraction of a specified collection from a specified set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/init(foraggregate:))*