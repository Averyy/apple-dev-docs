---
url: "https://docs.swift.org/latest/documentation/cxx/cxxspan"
framework: "Swift-Org/Cxx"
---

# CxxSpan

**Framework**: Swift-Org/Cxx  
**Kind**: protocol  
**Role**: Protocol

A C++ type that is an object that can refer to a contiguous sequence of objects.

## Declaration

```swift
protocol CxxSpan<Element>
```

## Overview

C++ standard library type `std::span` conforms to this protocol.

## Topics

### Associated Types
- [associatedtype Element : ~Copyable](./cxxspan/element.md)
- [associatedtype Size : BinaryInteger](./cxxspan/size.md)
### Initializers
- [init()](./cxxspan/init%28%29.md)
- [init(UnsafeMutableBufferPointer<Element>)](./cxxspan/init%28_%29-1orx7.md)
- [init(UnsafeBufferPointer<Element>)](./cxxspan/init%28_%29-73hp6.md)
  Creates a C++ span from a Swift UnsafeBufferPointer
- [init(Span<Element>)](./cxxspan/init%28_%29-749nt.md)
- [init(UnsafePointer<Element>!, Size)](./cxxspan/init%28_,_%29.md)
### Instance Methods
- [func size() -> Size](./cxxspan/size%28%29.md)

## See Also

### Sequences
- [protocol CxxSequence](./cxxsequence.md)
  Use this protocol to conform custom C++ sequence types to Swift’s `Sequence` protocol like this:
- [struct CxxIterator](./cxxiterator.md)
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxspan)*