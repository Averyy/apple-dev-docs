---
url: "https://docs.swift.org/latest/documentation/cxx/unsafecxxrandomaccessiterator"
framework: "Swift-Org/Cxx"
---

# UnsafeCxxRandomAccessIterator

**Framework**: Swift-Org/Cxx  
**Kind**: protocol  
**Role**: Protocol

Bridged C++ iterator that allows computing the distance between two of its instances, and advancing an instance by a given number of elements.

## Declaration

```swift
protocol UnsafeCxxRandomAccessIterator : UnsafeCxxInputIterator
```

#### Overview

Mostly useful for conforming a type to the `CxxRandomAccessCollection` protocol and should not generally be used directly.

> **See Also**: https://en.cppreference.com/w/cpp/named_req/RandomAccessIterator

## Topics

### Operators
- [static func += (inout Self, Distance)](./unsafecxxrandomaccessiterator/pluseq%28_,_%29.md)
- [static func - (Self, Self) -> Distance](./unsafecxxrandomaccessiterator/minus%28_,_%29.md)
### Associated Types
- [associatedtype Distance : BinaryInteger](./unsafecxxrandomaccessiterator/distance.md)

## Relationships

### Inherits From
- [Equatable](https://docs.swift.org/latest/documentation/swift/equatable)
- [UnsafeCxxInputIterator](./unsafecxxinputiterator.md)
### Inherited By
- [UnsafeCxxContiguousIterator](./unsafecxxcontiguousiterator.md)
- [UnsafeCxxMutableContiguousIterator](./unsafecxxmutablecontiguousiterator.md)
- [UnsafeCxxMutableRandomAccessIterator](./unsafecxxmutablerandomaccessiterator.md)
### Conforming Types
- [UnsafeMutablePointer](https://docs.swift.org/latest/documentation/swift/unsafemutablepointer)
- [UnsafePointer](https://docs.swift.org/latest/documentation/swift/unsafepointer)

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
- [protocol UnsafeCxxMutableContiguousIterator](./unsafecxxmutablecontiguousiterator.md)
- [protocol UnsafeCxxMutableInputIterator](./unsafecxxmutableinputiterator.md)
- [protocol UnsafeCxxMutableRandomAccessIterator](./unsafecxxmutablerandomaccessiterator.md)


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/unsafecxxrandomaccessiterator)*