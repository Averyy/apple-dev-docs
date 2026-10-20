# removals

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A collection of removal change objects.

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
var removals: [NSOrderedCollectionChange] { get }
```

```objc
@property (strong, readonly) NSArray<NSOrderedCollectionChange<id> *> * removals;
```

## See Also

### Accessing Changes
- [var hasChanges: Bool](./haschanges.md)
  A Boolean value that indicates if the difference has changes.
- [var insertions: [NSOrderedCollectionChange]](./insertions.md)
  A collection of insertion change objects.
- [class NSOrderedCollectionChange](../nsorderedcollectionchange.md)
  An object that represents an indexed change within an ordered collection.
- [enum NSCollectionChangeType](../nscollectionchangetype.md)
  The type of change represented in computing the difference of an ordered collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedcollectiondifference/removals)*