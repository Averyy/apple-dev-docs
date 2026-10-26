---
url: "https://docs.swift.org/latest/documentation/cxx/cxxrandomaccesscollection"
framework: "Swift-Org/Cxx"
---

# CxxRandomAccessCollection

**Framework**: Swift-Org/Cxx  
**Kind**: protocol  
**Role**: Protocol

## Declaration

```swift
protocol CxxRandomAccessCollection<Element> : CxxSequence, RandomAccessCollection where Self.RawIterator : UnsafeCxxRandomAccessIterator
```

## Topics

### Associated Types
- [associatedtype Element](./cxxrandomaccesscollection/element.md)
- [associatedtype Index = Int](./cxxrandomaccesscollection/index.md)
- [associatedtype Indices = Range<Int>](./cxxrandomaccesscollection/indices.md)
- [associatedtype Iterator = CxxIterator<Self>](./cxxrandomaccesscollection/iterator.md)
- [associatedtype RawIterator](./cxxrandomaccesscollection/rawiterator.md)
- [associatedtype SubSequence = Slice<Self>](./cxxrandomaccesscollection/subsequence.md)

## Relationships

### Inherits From
- [BidirectionalCollection](https://docs.swift.org/latest/documentation/swift/bidirectionalcollection)
- [Collection](https://docs.swift.org/latest/documentation/swift/collection)
- [CxxConvertibleToCollection](./cxxconvertibletocollection.md)
- [CxxSequence](./cxxsequence.md)
- [RandomAccessCollection](https://docs.swift.org/latest/documentation/swift/randomaccesscollection)
- [Sequence](https://docs.swift.org/latest/documentation/swift/sequence)
### Inherited By
- [CxxMutableRandomAccessCollection](./cxxmutablerandomaccesscollection.md)

## See Also

### Collections
- [protocol CxxDictionary](./cxxdictionary.md)
  A C++ type that represents a dictionary.
- [protocol CxxMutableRandomAccessCollection](./cxxmutablerandomaccesscollection.md)
- [protocol CxxVector](./cxxvector.md)
  A C++ type that represents a vector of values.
- [protocol CxxSet](./cxxset.md)
  A C++ type that represents a set of values, which might be repeating.
- [protocol CxxUniqueSet](./cxxuniqueset.md)
  A C++ type that represents a set of unique values.
- [protocol CxxPair](./cxxpair.md)
  A C++ type that represents a pair of two values.
- [protocol CxxConvertibleToCollection](./cxxconvertibletocollection.md)
  A C++ type that can be converted to a Swift collection.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxrandomaccesscollection)*