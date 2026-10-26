---
url: "https://docs.swift.org/latest/documentation/cxx/cxxmutablespan"
framework: "Swift-Org/Cxx"
---

# CxxMutableSpan

**Framework**: Swift-Org/Cxx  
**Kind**: protocol  
**Role**: Protocol

## Declaration

```swift
protocol CxxMutableSpan<Element>
```

## Topics

### Associated Types
- [associatedtype Element : ~Copyable](./cxxmutablespan/element.md)
- [associatedtype Size : BinaryInteger](./cxxmutablespan/size.md)
### Initializers
- [init()](./cxxmutablespan/init%28%29.md)
- [init(UnsafeMutableBufferPointer<Element>)](./cxxmutablespan/init%28_%29-2yxw9.md)
  Creates a C++ span from a Swift UnsafeMutableBufferPointer
- [init(consuming MutableSpan<Element>)](./cxxmutablespan/init%28_%29-6j9kz.md)
- [init(UnsafeMutablePointer<Element>!, Size)](./cxxmutablespan/init%28_,_%29.md)
### Instance Methods
- [func size() -> Size](./cxxmutablespan/size%28%29.md)

## See Also

### Sequences
- [protocol CxxSequence](./cxxsequence.md)
  Use this protocol to conform custom C++ sequence types to Swift’s `Sequence` protocol like this:
- [struct CxxIterator](./cxxiterator.md)
- [protocol CxxSpan](./cxxspan.md)
  A C++ type that is an object that can refer to a contiguous sequence of objects.
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxmutablespan)*