# NSFastEnumeration

**Framework**: Foundation  
**Kind**: protocol

A protocol that objects adopt to support fast enumeration.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol NSFastEnumeration
```

#### Overview

The abstract class [`NSEnumerator`](nsenumerator.md) provides a convenience implementation that uses [`nextObject()`](nsenumerator/nextobject().md) to return items one at a time.

## Topics

### Enumeration
- [func countByEnumerating(with: UnsafeMutablePointer<NSFastEnumerationState>, objects: AutoreleasingUnsafeMutablePointer<AnyObject?>, count: Int) -> Int](nsfastenumeration/countbyenumerating(with:objects:count:).md)
  Returns by reference a C array of objects over which the sender should iterate, and as the return value the number of objects in the array.
### Constants
- [struct NSFastEnumerationState](nsfastenumerationstate.md)
  This defines the structure used as contextual information in the [`NSFastEnumeration`](nsfastenumeration.md) protocol.

## Relationships

### Conforming Types
- [FileManager.DirectoryEnumerator](filemanager/directoryenumerator.md)
- [NSArray](nsarray.md)
- [NSCountedSet](nscountedset.md)
- [NSDictionary](nsdictionary.md)
- [NSEnumerator](nsenumerator.md)
- [NSHashTable](nshashtable.md)
- [NSMapTable](nsmaptable.md)
- [NSMutableArray](nsmutablearray.md)
- [NSMutableDictionary](nsmutabledictionary.md)
- [NSMutableOrderedSet](nsmutableorderedset.md)
- [NSMutableSet](nsmutableset.md)
- [NSOrderedCollectionDifference](nsorderedcollectiondifference.md)
- [NSOrderedSet](nsorderedset.md)
- [NSPointerArray](nspointerarray.md)
- [NSSet](nsset.md)

## See Also

- [class NSEnumerator](nsenumerator.md)
  An abstract class whose subclasses enumerate collections of objects, such as arrays and dictionaries.
- [struct NSFastEnumerationIterator](nsfastenumerationiterator.md)
- [struct NSIndexSetIterator](nsindexsetiterator.md)
  An iterator suitable for enumerating the elements of an index set.
- [struct NSEnumerationOptions](nsenumerationoptions.md)
  Options for block enumeration operations.
- [struct NSSortOptions](nssortoptions.md)
  Options for block sorting operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfastenumeration)*