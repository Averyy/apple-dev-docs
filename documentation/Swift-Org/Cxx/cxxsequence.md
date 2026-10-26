---
url: "https://docs.swift.org/latest/documentation/cxx/cxxsequence"
framework: "Swift-Org/Cxx"
---

# CxxSequence

**Framework**: Swift-Org/Cxx  
**Kind**: protocol  
**Role**: Protocol

Use this protocol to conform custom C++ sequence types to Swift’s `Sequence` protocol like this:

## Declaration

```swift
protocol CxxSequence<Element> : CxxConvertibleToCollection, Sequence
```

#### Overview

```swift
extension MyCxxSequenceType : CxxSequence {}
```

This requires the C++ sequence type to define const methods `begin()` and `end()` which return input iterators into the C++ sequence. The iterator types must conform to `UnsafeCxxInputIterator`.

## Topics

### Associated Types
- [associatedtype Element](./cxxsequence/element.md)
- [associatedtype Iterator = CxxIterator<Self>](./cxxsequence/iterator.md)
- [associatedtype RawIterator](./cxxsequence/rawiterator.md)

## Relationships

### Inherits From
- [CxxConvertibleToCollection](./cxxconvertibletocollection.md)
- [Sequence](https://docs.swift.org/latest/documentation/swift/sequence)
### Inherited By
- [CxxMutableRandomAccessCollection](./cxxmutablerandomaccesscollection.md)
- [CxxRandomAccessCollection](./cxxrandomaccesscollection.md)

## See Also

### Sequences
- [struct CxxIterator](./cxxiterator.md)
- [protocol CxxSpan](./cxxspan.md)
  A C++ type that is an object that can refer to a contiguous sequence of objects.
- [protocol CxxMutableSpan](./cxxmutablespan.md)
- [protocol UnsafeCxxContiguousIterator](./unsafecxxcontiguousiterator.md)
  Bridged C++ iterator that allows traversing elements of a random access collection that are stored in contiguous memory segments.
- [protocol UnsafeCxxInputIterator](./unsafecxxinputiterator.md)
  Bridged C++ iterator that allows to traverse the elements of a sequence using a for-in loop.
- [protocol UnsafeCxxMutableContiguousIterator](./unsafecxxmutablecontiguousiterator.md)
- [protocol UnsafeCxxMutableInputIterator](./unsafecxxmutableinputiterator.md)
- [protocol UnsafeCxxMutableRandomAccessIterator](./unsafecxxmutablerandomaccessiterator.md)
- [protocol UnsafeCxxRandomAccessIterator](./unsafecxxrandomaccessiterator.md)
  Bridged C++ iterator that allows computing the distance between two of its instances, and advancing an instance by a given number of elements.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxsequence)*