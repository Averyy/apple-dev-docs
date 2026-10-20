# NSOrderedCollectionDifference

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

An object representing the difference between two ordered collections.

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
class NSOrderedCollectionDifference
```

```objc
@interface NSOrderedCollectionDifference : NSObject
```

#### Overview

Use [`differenceFromArray:`](./nsarray/differencefromarray_.md) or one of its variations to get an instance of [`NSOrderedCollectionDifference`](./nsorderedcollectiondifference.md), which represents the difference between two ordered collections.

For example, the following sample compares two arrays of strings to create a difference that represents the changes:

```objc
NSArray *original = @[@"Red", @"Green", @"Blue"];
NSArray *modified = @[@"Red", @"Blue", @"Green"];

NSOrderedCollectionDifference *diff = [original differenceFromArray:modified];

// diff.hasChanges == TRUE
// diff.insertions.count == 1
// diff.removals.count == 1

```

## Topics

### Accessing Changes
- [var hasChanges: Bool](./nsorderedcollectiondifference/haschanges.md)
  A Boolean value that indicates if the difference has changes.
- [var insertions: [NSOrderedCollectionChange]](./nsorderedcollectiondifference/insertions.md)
  A collection of insertion change objects.
- [var removals: [NSOrderedCollectionChange]](./nsorderedcollectiondifference/removals.md)
  A collection of removal change objects.
- [class NSOrderedCollectionChange](./nsorderedcollectionchange.md)
  An object that represents an indexed change within an ordered collection.
- [enum NSCollectionChangeType](./nscollectionchangetype.md)
  The type of change represented in computing the difference of an ordered collection.
### Inverting a Difference Object
- [func inverse() -> Self](./nsorderedcollectiondifference/inverse%28%29.md)
  Calculate the difference between two objects in the reverse direction of comparison.
### Creating a Collection Difference Object
- [convenience init(changes: [NSOrderedCollectionChange])](./nsorderedcollectiondifference/init%28changes%29.md)
  Creates an ordered collection difference using an array of ordered collection changes.
- [convenience init(insert: IndexSet, insertedObjects: [Any]?, remove: IndexSet, removedObjects: [Any]?)](./nsorderedcollectiondifference/init%28insert,insertedobjects,remove,removedobjects%29.md)
  Creates an ordered collection difference from arrays of inserted and removed objects with corresponding sets of indices.
- [init(insert: IndexSet, insertedObjects: [Any]?, remove: IndexSet, removedObjects: [Any]?, additionalChanges: [NSOrderedCollectionChange])](./nsorderedcollectiondifference/init%28insert,insertedobjects,remove,removedobjects,additionalchanges%29.md)
  Creates an ordered collection difference from arrays of inserted and removed objects with corresponding sets of indices, in addition to an array of ordered collection changes.
### Updating Changes from a Difference Object
- [func transformingChanges((NSOrderedCollectionChange) -> NSOrderedCollectionChange) -> CollectionDifference<Any>](./nsorderedcollectiondifference/transformingchanges%28_%29.md)
  Create a new ordered collection difference by mapping over this difference’s members, processing the change objects with the block provided.
### Initializers
- [convenience init(insertIndexes: IndexSet, insertedObjects: [Any]?, removeIndexes: IndexSet, removedObjects: [Any]?)](./nsorderedcollectiondifference/init%28insertindexes,insertedobjects,removeindexes,removedobjects%29.md)
- [init(insertIndexes: IndexSet, insertedObjects: [Any]?, removeIndexes: IndexSet, removedObjects: [Any]?, additionalChanges: [NSOrderedCollectionChange])](./nsorderedcollectiondifference/init%28insertindexes,insertedobjects,removeindexes,removedobjects,additionalchanges%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSFastEnumeration](./nsfastenumeration.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Comparing with Another Array
- [struct NSOrderedCollectionDifferenceCalculationOptions](./nsorderedcollectiondifferencecalculationoptions.md)
  Constants that specify the options to use when creating an ordered collection difference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedcollectiondifference)*