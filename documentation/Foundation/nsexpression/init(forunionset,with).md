# init(forUnionSet:with:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates an expression object that represents the union of a specified set and collection.

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
init(forUnionSet left: NSExpression, with right: NSExpression)
```

```objc
+ (NSExpression *) expressionForUnionSet:(NSExpression *) left with:(NSExpression *) right;
```

## Return Value

An new `NSExpression` object that represents the union of `left` and `right`.

## Parameters

- `left`: An expression that evaluates to an `NSSet` object.
- `right`: An expression that evaluates to a collection object (an instance of `NSArray`, `NSSet`, or `NSDictionary`).

## See Also

### Creating a Collection Expression
- [init(forAggregate: [NSExpression])](./init%28foraggregate%29.md)
  Creates an aggregate expression for a specified collection.
- [init(forIntersectSet: NSExpression, with: NSExpression)](./init%28forintersectset,with%29.md)
  Creates an expression object that represents the intersection of a specified set and collection.
- [init(forMinusSet: NSExpression, with: NSExpression)](./init%28forminusset,with%29.md)
  Creates an expression object that represents the subtraction of a specified collection from a specified set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/init(forunionset:with:))*