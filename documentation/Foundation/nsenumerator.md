# NSEnumerator

**Framework**: Foundation  
**Kind**: class

An abstract class whose subclasses enumerate collections of objects, such as arrays and dictionaries.

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
class NSEnumerator
```

#### Overview

All creation methods are defined in the collection classes—such as [`NSArray`](nsarray.md), [`NSSet`](nsset.md), and [`NSDictionary`](nsdictionary.md)—which provide special [`NSEnumerator`](nsenumerator.md) objects with which to enumerate their contents. For example, `NSArray` has two methods that return an [`NSEnumerator`](nsenumerator.md) object: [`objectEnumerator()`](nsset/objectenumerator().md) and [`reverseObjectEnumerator()`](nsarray/reverseobjectenumerator().md). `NSDictionary` also has two methods that return an [`NSEnumerator`](nsenumerator.md) object: [`keyEnumerator()`](nsdictionary/keyenumerator().md) and [`objectEnumerator()`](nsdictionary/objectenumerator().md). These methods let you enumerate the contents of a dictionary by key or by value, respectively.

You send [`nextObject()`](nsenumerator/nextobject().md) repeatedly to a newly created [`NSEnumerator`](nsenumerator.md) object to have it return the next object in the original collection. When the collection is exhausted, `nil` is returned. You cannot “reset” an enumerator after it has exhausted its collection. To enumerate a collection again, you need a new enumerator.

The enumerator subclasses used by `NSArray`, `NSDictionary`, and `NSSet` retain the collection during enumeration. When the enumeration is exhausted, the collection is released.

> **Note**:  In Objective-C, it is not safe to modify a mutable collection while enumerating through it. Some enumerators may currently allow enumeration of a collection that is modified, but this behavior is not guaranteed to be supported in the future.

 In Objective-C, it is not safe to modify a mutable collection while enumerating through it. Some enumerators may currently allow enumeration of a collection that is modified, but this behavior is not guaranteed to be supported in the future.

## Topics

### Getting the Enumerated Objects
- [var allObjects: [Any]](nsenumerator/allobjects.md)
  The array of unenumerated objects.
- [func nextObject() -> Any?](nsenumerator/nextobject.md)
  Returns the next object from the collection being enumerated.
### Default Implementations
- [Sequence Implementations](nsenumerator/sequence-implementations.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [FileManager.DirectoryEnumerator](filemanager/directoryenumerator.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSFastEnumeration](nsfastenumeration.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [protocol NSFastEnumeration](nsfastenumeration.md)
  A protocol that objects adopt to support fast enumeration.
- [struct NSFastEnumerationIterator](nsfastenumerationiterator.md)
- [struct NSIndexSetIterator](nsindexsetiterator.md)
  An iterator suitable for enumerating the elements of an index set.
- [struct NSEnumerationOptions](nsenumerationoptions.md)
  Options for block enumeration operations.
- [struct NSSortOptions](nssortoptions.md)
  Options for block sorting operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsenumerator)*