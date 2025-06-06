# NSOrderedCollectionChange

**Framework**: Foundation  
**Kind**: class

An object that represents an indexed change within an ordered collection.

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
class NSOrderedCollectionChange
```

#### Overview

An ordered collection change represents changes by adding, removing, or moving objects within an ordered collection. Changes with an associated index indicate a move within the collection.

## Topics

### Creating a Change
- [convenience init(object: Any?, type: NSCollectionChangeType, index: Int)](nsorderedcollectionchange/init(object:type:index:).md)
  Creates a change object that represents inserting or removing an object from an ordered collection at a specific index.
- [init(object: Any?, type: NSCollectionChangeType, index: Int, associatedIndex: Int)](nsorderedcollectionchange/init(object:type:index:associatedindex:).md)
  Creates a change object that represents inserting, removing, or moving an object from an ordered collection at a specific index.
### Accessing the Change
- [var changeType: NSCollectionChangeType](nsorderedcollectionchange/changetype.md)
  The type of change.
- [var index: Int](nsorderedcollectionchange/index.md)
  The index location of the change.
- [var object: Any?](nsorderedcollectionchange/object.md)
  An object the change inserts or removes.
- [var associatedIndex: Int](nsorderedcollectionchange/associatedindex.md)
  When this property is set to a value other than [`NSNotFound`](nsnotfound-9t5v2.md), the receiver is one half of a move, and this value is the index of the change’s counterpart of the opposite type in the diff.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var hasChanges: Bool](nsorderedcollectiondifference/haschanges.md)
  A Boolean value that indicates if the difference has changes.
- [var insertions: [NSOrderedCollectionChange]](nsorderedcollectiondifference/insertions.md)
  A collection of insertion change objects.
- [var removals: [NSOrderedCollectionChange]](nsorderedcollectiondifference/removals.md)
  A collection of removal change objects.
- [enum NSCollectionChangeType](nscollectionchangetype.md)
  The type of change represented in computing the difference of an ordered collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsorderedcollectionchange)*