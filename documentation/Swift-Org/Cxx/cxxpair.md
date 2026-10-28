---
url: "https://docs.swift.org/latest/documentation/cxx/cxxpair"
framework: "Swift-Org/Cxx"
---

# CxxPair

**Framework**: Swift-Org/Cxx  
**Kind**: protocol  
**Role**: Protocol

A C++ type that represents a pair of two values.

## Declaration

```swift
protocol CxxPair<First, Second> : ~Copyable
```

## Overview

C++ standard library type `std::pair` conforms to this protocol.

## Topics

### Associated Types
- [associatedtype First : ~Copyable](./cxxpair/first-swift.associatedtype.md)
- [associatedtype Second : ~Copyable](./cxxpair/second-swift.associatedtype.md)
### Initializers
- [init(first: consuming First, second: consuming Second)](./cxxpair/init%28first,second%29.md)
### Instance Properties
- [var first: First](./cxxpair/first-swift.property.md)
- [var second: Second](./cxxpair/second-swift.property.md)

## See Also

### Collections
- [protocol CxxDictionary](./cxxdictionary.md)
  A C++ type that represents a dictionary.
- [protocol CxxRandomAccessCollection](./cxxrandomaccesscollection.md)
- [protocol CxxMutableRandomAccessCollection](./cxxmutablerandomaccesscollection.md)
- [protocol CxxVector](./cxxvector.md)
  A C++ type that represents a vector of values.
- [protocol CxxSet](./cxxset.md)
  A C++ type that represents a set of values, which might be repeating.
- [protocol CxxUniqueSet](./cxxuniqueset.md)
  A C++ type that represents a set of unique values.
- [protocol CxxConvertibleToCollection](./cxxconvertibletocollection.md)
  A C++ type that can be converted to a Swift collection.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxpair)*