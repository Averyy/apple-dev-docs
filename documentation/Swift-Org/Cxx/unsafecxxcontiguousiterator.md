---
url: "https://docs.swift.org/latest/documentation/cxx/unsafecxxcontiguousiterator"
framework: "Swift-Org/Cxx"
---

# UnsafeCxxContiguousIterator

**Framework**: Swift-Org/Cxx  
**Kind**: protocol  
**Role**: Protocol

Bridged C++ iterator that allows traversing elements of a random access collection that are stored in contiguous memory segments.

## Declaration

```swift
protocol UnsafeCxxContiguousIterator : UnsafeCxxRandomAccessIterator
```

## Overview

Mostly useful for optimizing operations with containers that conform to `CxxRandomAccessCollection` and should not generally be used directly.

> **See Also**: https://en.cppreference.com/w/cpp/named_req/ContiguousIterator

## Relationships

### Inherits From
- [Equatable](https://docs.swift.org/latest/documentation/swift/equatable)
- [UnsafeCxxInputIterator](./unsafecxxinputiterator.md)
- [UnsafeCxxRandomAccessIterator](./unsafecxxrandomaccessiterator.md)
### Inherited By
- [UnsafeCxxMutableContiguousIterator](./unsafecxxmutablecontiguousiterator.md)

## See Also

### Sequences
- [protocol CxxSequence](./cxxsequence.md)
  Use this protocol to conform custom C++ sequence types to Swift’s `Sequence` protocol like this:
- [struct CxxIterator](./cxxiterator.md)
- [protocol CxxSpan](./cxxspan.md)
  A C++ type that is an object that can refer to a contiguous sequence of objects.
- [protocol CxxMutableSpan](./cxxmutablespan.md)
- [protocol UnsafeCxxInputIterator](./unsafecxxinputiterator.md)
  Bridged C++ iterator that allows to traverse the elements of a sequence using a for-in loop.
- [protocol UnsafeCxxMutableContiguousIterator](./unsafecxxmutablecontiguousiterator.md)
- [protocol UnsafeCxxMutableInputIterator](./unsafecxxmutableinputiterator.md)
- [protocol UnsafeCxxMutableRandomAccessIterator](./unsafecxxmutablerandomaccessiterator.md)
- [protocol UnsafeCxxRandomAccessIterator](./unsafecxxrandomaccessiterator.md)
  Bridged C++ iterator that allows computing the distance between two of its instances, and advancing an instance by a given number of elements.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/unsafecxxcontiguousiterator)*