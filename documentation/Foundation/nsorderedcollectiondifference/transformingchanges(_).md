# transformingChanges(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Create a new ordered collection difference by mapping over this difference’s members, processing the change objects with the block provided.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func transformingChanges(_ block: (NSOrderedCollectionChange) -> NSOrderedCollectionChange) -> CollectionDifference<Any>
```

```objc
- (NSOrderedCollectionDifference<id> *) differenceByTransformingChangesWithBlock:(NSOrderedCollectionChange<id> * (^)(NSOrderedCollectionChange<id> *)) block;
```

## Return Value

A new ordered collection difference.

## Parameters

- `block`: A block receives an ordered collection change and returns an updated change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedcollectiondifference/transformingchanges(_:))*