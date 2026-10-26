---
url: "https://docs.swift.org/latest/documentation/cxx/cxxset"
framework: "Swift-Org/Cxx"
---

# CxxSet

**Framework**: Swift-Org/Cxx  
**Kind**: protocol  
**Role**: Protocol

A C++ type that represents a set of values, which might be repeating.

## Declaration

```swift
protocol CxxSet<Element> : ExpressibleByArrayLiteral
```

#### Overview

C++ standard library types such as `std::set`, `std::unordered_set` and `std::multiset` conform to this protocol.

> **See Also**: `CxxUniqueSet`

## Topics

### Associated Types
- [associatedtype Element](./cxxset/element.md)
- [associatedtype InsertionResult](./cxxset/insertionresult.md)
- [associatedtype RawIterator : UnsafeCxxInputIterator](./cxxset/rawiterator.md)
- [associatedtype RawMutableIterator : UnsafeCxxInputIterator](./cxxset/rawmutableiterator.md)
- [associatedtype Size : BinaryInteger](./cxxset/size.md)
### Initializers
- [init()](./cxxset/init%28%29.md)
- [init<S>(S)](./cxxset/init%28_%29.md)
  Creates a C++ set containing the elements of a Swift Sequence.
### Instance Methods
- [func contains(Element) -> Bool](./cxxset/contains%28_%29.md)
  Returns a Boolean value that indicates whether the given element exists in the set.
- [func count(Element) -> Size](./cxxset/count%28_%29.md)

## Relationships

### Inherits From
- [ExpressibleByArrayLiteral](https://docs.swift.org/latest/documentation/swift/expressiblebyarrayliteral)
### Inherited By
- [CxxUniqueSet](./cxxuniqueset.md)

## See Also

### Collections
- [protocol CxxDictionary](./cxxdictionary.md)
  A C++ type that represents a dictionary.
- [protocol CxxRandomAccessCollection](./cxxrandomaccesscollection.md)
- [protocol CxxMutableRandomAccessCollection](./cxxmutablerandomaccesscollection.md)
- [protocol CxxVector](./cxxvector.md)
  A C++ type that represents a vector of values.
- [protocol CxxUniqueSet](./cxxuniqueset.md)
  A C++ type that represents a set of unique values.
- [protocol CxxPair](./cxxpair.md)
  A C++ type that represents a pair of two values.
- [protocol CxxConvertibleToCollection](./cxxconvertibletocollection.md)
  A C++ type that can be converted to a Swift collection.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxset)*