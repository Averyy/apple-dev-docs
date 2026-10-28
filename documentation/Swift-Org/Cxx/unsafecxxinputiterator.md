---
url: "https://docs.swift.org/latest/documentation/cxx/unsafecxxinputiterator"
framework: "Swift-Org/Cxx"
---

# UnsafeCxxInputIterator

**Framework**: Swift-Org/Cxx  
**Kind**: protocol  
**Role**: Protocol

Bridged C++ iterator that allows to traverse the elements of a sequence using a for-in loop.

## Declaration

```swift
protocol UnsafeCxxInputIterator : Equatable
```

## Overview

Mostly useful for conforming a type to the `CxxSequence` protocol. Do not directly use this protocol in Swift.

> **See Also**: https://en.cppreference.com/w/cpp/named_req/InputIterator

## Topics

### Associated Types
- [associatedtype DereferenceResult](./unsafecxxinputiterator/dereferenceresult.md)
- [associatedtype Pointee : ~Copyable](./unsafecxxinputiterator/pointee-swift.associatedtype.md)
### Instance Properties
- [var pointee: Pointee](./unsafecxxinputiterator/pointee-swift.property.md)
  Returns the unwrapped result of C++ `operator*()`.
### Instance Methods
- [func successor() -> Self](./unsafecxxinputiterator/successor%28%29.md)
  Returns an iterator pointing to the next item in the sequence.

## Relationships

### Inherits From
- [Equatable](https://docs.swift.org/latest/documentation/swift/equatable)
### Inherited By
- [UnsafeCxxContiguousIterator](./unsafecxxcontiguousiterator.md)
- [UnsafeCxxMutableContiguousIterator](./unsafecxxmutablecontiguousiterator.md)
- [UnsafeCxxMutableInputIterator](./unsafecxxmutableinputiterator.md)
- [UnsafeCxxMutableRandomAccessIterator](./unsafecxxmutablerandomaccessiterator.md)
- [UnsafeCxxRandomAccessIterator](./unsafecxxrandomaccessiterator.md)
### Conforming Types
- [Optional](https://docs.swift.org/latest/documentation/swift/optional)
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
- [protocol UnsafeCxxMutableContiguousIterator](./unsafecxxmutablecontiguousiterator.md)
- [protocol UnsafeCxxMutableInputIterator](./unsafecxxmutableinputiterator.md)
- [protocol UnsafeCxxMutableRandomAccessIterator](./unsafecxxmutablerandomaccessiterator.md)
- [protocol UnsafeCxxRandomAccessIterator](./unsafecxxrandomaccessiterator.md)
  Bridged C++ iterator that allows computing the distance between two of its instances, and advancing an instance by a given number of elements.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/unsafecxxinputiterator)*