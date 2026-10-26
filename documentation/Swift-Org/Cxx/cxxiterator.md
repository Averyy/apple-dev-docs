---
url: "https://docs.swift.org/latest/documentation/cxx/cxxiterator"
framework: "Swift-Org/Cxx"
---

# CxxIterator

**Framework**: Swift-Org/Cxx  
**Kind**: struct  
**Role**: Structure

## Declaration

```swift
@frozen
struct CxxIterator<T> where T : CxxSequence
```

## Topics

### Initializers
- [init(sequence: T)](./cxxiterator/init%28sequence%29.md)
### Instance Methods
- [func next() -> Element?](./cxxiterator/next%28%29.md)
### Type Aliases
- [CxxIterator.Element](./cxxiterator/element.md)

## Relationships

### Conforms To
- [IteratorProtocol](https://docs.swift.org/latest/documentation/swift/iteratorprotocol)

## See Also

### Sequences
- [protocol CxxSequence](./cxxsequence.md)
  Use this protocol to conform custom C++ sequence types to Swift’s `Sequence` protocol like this:
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxiterator)*