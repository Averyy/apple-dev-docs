# NSIndexSetIterator

**Framework**: Foundation  
**Kind**: struct

An iterator suitable for enumerating the elements of an index set.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct NSIndexSetIterator
```

#### Overview

You typically obtain an index set iterator by calling the [`makeIterator()`](nsindexset/makeiterator().md) function of an [`NSIndexSet`](nsindexset.md) instance.

## Relationships

### Conforms To
- [IteratorProtocol](../Swift/IteratorProtocol.md)

## See Also

- [class NSEnumerator](nsenumerator.md)
  An abstract class whose subclasses enumerate collections of objects, such as arrays and dictionaries.
- [protocol NSFastEnumeration](nsfastenumeration.md)
  A protocol that objects adopt to support fast enumeration.
- [struct NSFastEnumerationIterator](nsfastenumerationiterator.md)
- [struct NSEnumerationOptions](nsenumerationoptions.md)
  Options for block enumeration operations.
- [struct NSSortOptions](nssortoptions.md)
  Options for block sorting operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexsetiterator)*