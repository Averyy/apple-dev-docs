---
url: "https://docs.swift.org/latest/documentation/cxx/cxxconvertibletocollection"
framework: "Swift-Org/Cxx"
---

# CxxConvertibleToCollection

**Framework**: Swift-Org/Cxx  
**Kind**: protocol  
**Role**: Protocol

A C++ type that can be converted to a Swift collection.

## Declaration

```swift
protocol CxxConvertibleToCollection<Element>
```

## Topics

### Associated Types
- [associatedtype Element](./cxxconvertibletocollection/element.md)
- [associatedtype RawIterator : UnsafeCxxInputIterator](./cxxconvertibletocollection/rawiterator.md)
### Instance Methods
- [func forEach((Element) throws -> Void) rethrows](./cxxconvertibletocollection/foreach%28_%29-5ds8r.md)
- [func forEach((RawIterator.Pointee) throws -> Void) rethrows](./cxxconvertibletocollection/foreach%28_%29-7bkbm.md)

## Relationships

### Inherited By
- [CxxMutableRandomAccessCollection](./cxxmutablerandomaccesscollection.md)
- [CxxRandomAccessCollection](./cxxrandomaccesscollection.md)
- [CxxSequence](./cxxsequence.md)

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
- [protocol CxxPair](./cxxpair.md)
  A C++ type that represents a pair of two values.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxconvertibletocollection)*