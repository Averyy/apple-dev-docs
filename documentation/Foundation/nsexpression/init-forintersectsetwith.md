# init(forIntersectSet:with:)

**Framework**: Foundation  
**Kind**: init

Creates an expression object that represents the intersection of a specified set and collection.

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
init(forIntersectSet left: NSExpression, with right: NSExpression)
```

#### Return Value

A new `NSExpression` object that represents the intersection of `left` and `right`.

## Parameters

- `left`: An expression that evaluates to an   object.
- `right`: An expression that evaluates to a collection object (an instance of  ,  , or  ).

## See Also

- [init(forAggregate: [NSExpression])](nsexpression/init(foraggregate:).md)
  Creates an aggregate expression for a specified collection.
- [init(forUnionSet: NSExpression, with: NSExpression)](nsexpression/init(forunionset:with:).md)
  Creates an expression object that represents the union of a specified set and collection.
- [init(forMinusSet: NSExpression, with: NSExpression)](nsexpression/init(forminusset:with:).md)
  Creates an expression object that represents the subtraction of a specified collection from a specified set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsexpression/init(forintersectset:with:))*