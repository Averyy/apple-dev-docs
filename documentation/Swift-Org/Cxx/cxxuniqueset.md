---
url: "https://docs.swift.org/latest/documentation/cxx/cxxuniqueset"
framework: "Swift-Org/Cxx"
---

# CxxUniqueSet

**Framework**: Swift-Org/Cxx  
**Kind**: protocol  
**Role**: Protocol

A C++ type that represents a set of unique values.

## Declaration

```swift
protocol CxxUniqueSet<Element> : CxxSet where Self.InsertionResult : CxxPair, Self.RawMutableIterator == Self.InsertionResult.First, Self.InsertionResult.Second == Bool
```

#### Overview

C++ standard library types such as `std::set` and `std::unordered_set` conform to this protocol.

## Topics

### Associated Types
- [associatedtype InsertionResult](./cxxuniqueset/insertionresult.md)
### Instance Methods
- [func insert(Element) -> (inserted: Bool, memberAfterInsert: Element)](./cxxuniqueset/insert%28_%29.md)
  Inserts the given element in the set if it is not already present.
- [func remove(Element) -> Element?](./cxxuniqueset/remove%28_%29.md)
  Removes the given element from the set.

## Relationships

### Inherits From
- [CxxSet](./cxxset.md)
- [ExpressibleByArrayLiteral](https://docs.swift.org/latest/documentation/swift/expressiblebyarrayliteral)

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
- [protocol CxxPair](./cxxpair.md)
  A C++ type that represents a pair of two values.
- [protocol CxxConvertibleToCollection](./cxxconvertibletocollection.md)
  A C++ type that can be converted to a Swift collection.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxuniqueset)*