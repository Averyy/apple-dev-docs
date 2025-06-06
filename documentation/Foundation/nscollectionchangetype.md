# NSCollectionChangeType

**Framework**: Foundation  
**Kind**: enum

The type of change represented in computing the difference of an ordered collection.

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
enum NSCollectionChangeType
```

## Topics

### Types of Ordered Collection Changes
- [NSCollectionChangeType.insert](nscollectionchangetype/insert.md)
  A change type that represents the insertion of an object into an ordered collection.
- [NSCollectionChangeType.remove](nscollectionchangetype/remove.md)
  A change type that represents the removal of an object from an ordered collection.
### Initializers
- [init?(rawValue: Int)](nscollectionchangetype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var hasChanges: Bool](nsorderedcollectiondifference/haschanges.md)
  A Boolean value that indicates if the difference has changes.
- [var insertions: [NSOrderedCollectionChange]](nsorderedcollectiondifference/insertions.md)
  A collection of insertion change objects.
- [var removals: [NSOrderedCollectionChange]](nsorderedcollectiondifference/removals.md)
  A collection of removal change objects.
- [class NSOrderedCollectionChange](nsorderedcollectionchange.md)
  An object that represents an indexed change within an ordered collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscollectionchangetype)*