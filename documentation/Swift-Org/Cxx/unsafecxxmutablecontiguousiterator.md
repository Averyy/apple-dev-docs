---
url: "https://docs.swift.org/latest/documentation/cxx/unsafecxxmutablecontiguousiterator"
framework: "Swift-Org/Cxx"
---

# UnsafeCxxMutableContiguousIterator

**Framework**: Swift-Org/Cxx  
**Kind**: protocol  
**Role**: Protocol

## Declaration

```swift
protocol UnsafeCxxMutableContiguousIterator : UnsafeCxxContiguousIterator, UnsafeCxxMutableRandomAccessIterator
```

## Relationships

### Inherits From
- [Equatable](https://docs.swift.org/latest/documentation/swift/equatable)
- [UnsafeCxxContiguousIterator](./unsafecxxcontiguousiterator.md)
- [UnsafeCxxInputIterator](./unsafecxxinputiterator.md)
- [UnsafeCxxMutableInputIterator](./unsafecxxmutableinputiterator.md)
- [UnsafeCxxMutableRandomAccessIterator](./unsafecxxmutablerandomaccessiterator.md)
- [UnsafeCxxRandomAccessIterator](./unsafecxxrandomaccessiterator.md)

## See Also

### Sequences
- [protocol CxxSequence](./cxxsequence.md)
  Use this protocol to conform custom C++ sequence types to Swift’s `Sequence` protocol like this:
- [struct CxxIterator](./cxxiterator.md)
- [protocol CxxSpan](./cxxspan.md)
  A C++ type that is an object that can refer to a contiguous sequence of objects.
- [protocol CxxMutableSpan](./cxxmutablespan.md)
- [protocol UnsafeCxxContiguousIterator](./unsafecxxcontiguousiterator.md)
  Bridged C++ iterator that allows traversing elements of a random access collection that are stored in contiguous memory segments.
- [protocol UnsafeCxxInputIterator](./unsafecxxinputiterator.md)
  Bridged C++ iterator that allows to traverse the elements of a sequence using a for-in loop.
- [protocol UnsafeCxxMutableInputIterator](./unsafecxxmutableinputiterator.md)
- [protocol UnsafeCxxMutableRandomAccessIterator](./unsafecxxmutablerandomaccessiterator.md)
- [protocol UnsafeCxxRandomAccessIterator](./unsafecxxrandomaccessiterator.md)
  Bridged C++ iterator that allows computing the distance between two of its instances, and advancing an instance by a given number of elements.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/unsafecxxmutablecontiguousiterator)*