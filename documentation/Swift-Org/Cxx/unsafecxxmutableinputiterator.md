---
url: "https://docs.swift.org/latest/documentation/cxx/unsafecxxmutableinputiterator"
framework: "Swift-Org/Cxx"
---

# UnsafeCxxMutableInputIterator

**Framework**: Swift-Org/Cxx  
**Kind**: protocol  
**Role**: Protocol

## Declaration

```swift
protocol UnsafeCxxMutableInputIterator : UnsafeCxxInputIterator
```

## Topics

### Instance Properties
- [var pointee: Pointee](./unsafecxxmutableinputiterator/pointee.md)

## Relationships

### Inherits From
- [Equatable](https://docs.swift.org/latest/documentation/swift/equatable)
- [UnsafeCxxInputIterator](./unsafecxxinputiterator.md)
### Inherited By
- [UnsafeCxxMutableContiguousIterator](./unsafecxxmutablecontiguousiterator.md)
- [UnsafeCxxMutableRandomAccessIterator](./unsafecxxmutablerandomaccessiterator.md)
### Conforming Types
- [UnsafeMutablePointer](https://docs.swift.org/latest/documentation/swift/unsafemutablepointer)

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
- [protocol UnsafeCxxMutableRandomAccessIterator](./unsafecxxmutablerandomaccessiterator.md)
- [protocol UnsafeCxxRandomAccessIterator](./unsafecxxrandomaccessiterator.md)
  Bridged C++ iterator that allows computing the distance between two of its instances, and advancing an instance by a given number of elements.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/unsafecxxmutableinputiterator)*