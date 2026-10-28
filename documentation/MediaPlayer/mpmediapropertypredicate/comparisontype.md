# comparisonType

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The type of matching comparison that the media property predicate performs when you invoke a query.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var comparisonType: MPMediaPredicateComparison { get }
```

```objc
@property (nonatomic, readonly) MPMediaPredicateComparison comparisonType;
```

## Discussion

For comparison types, see [`MPMediaPredicateComparison`](../mpmediapredicatecomparison.md).

## See Also

### Examining media property predicates
- [var property: String](./property.md)
  The property that the media property predicate uses when you invoke a query.
- [var value: Any?](./value.md)
  The value that the media property predicate matches against when you invoke a query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediapropertypredicate/comparisontype)*