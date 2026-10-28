---
url: "https://docs.swift.org/latest/documentation/cxx/cxxvector"
framework: "Swift-Org/Cxx"
---

# CxxVector

**Framework**: Swift-Org/Cxx  
**Kind**: protocol  
**Role**: Protocol

A C++ type that represents a vector of values.

## Declaration

```swift
protocol CxxVector<Element> : ExpressibleByArrayLiteral
```

## Overview

C++ standard library type `std::vector` conforms to this protocol.

## Topics

### Associated Types
- [associatedtype Element](./cxxvector/element.md)
- [associatedtype RawIterator : UnsafeCxxRandomAccessIterator](./cxxvector/rawiterator.md)
- [associatedtype Size : BinaryInteger](./cxxvector/size.md)
### Initializers
- [init()](./cxxvector/init%28%29.md)
- [init<S>(S)](./cxxvector/init%28_%29.md)
  Creates a C++ vector containing the elements of a Swift Sequence.
### Instance Properties
- [var span: Span<Element>](./cxxvector/span.md)
### Instance Methods
- [func push_back(Element)](./cxxvector/push_back%28_%29.md)
- [func size() -> Size](./cxxvector/size%28%29.md)

## Relationships

### Inherits From
- [ExpressibleByArrayLiteral](https://docs.swift.org/latest/documentation/swift/expressiblebyarrayliteral)

## See Also

### Collections
- [protocol CxxDictionary](./cxxdictionary.md)
  A C++ type that represents a dictionary.
- [protocol CxxRandomAccessCollection](./cxxrandomaccesscollection.md)
- [protocol CxxMutableRandomAccessCollection](./cxxmutablerandomaccesscollection.md)
- [protocol CxxSet](./cxxset.md)
  A C++ type that represents a set of values, which might be repeating.
- [protocol CxxUniqueSet](./cxxuniqueset.md)
  A C++ type that represents a set of unique values.
- [protocol CxxPair](./cxxpair.md)
  A C++ type that represents a pair of two values.
- [protocol CxxConvertibleToCollection](./cxxconvertibletocollection.md)
  A C++ type that can be converted to a Swift collection.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxvector)*