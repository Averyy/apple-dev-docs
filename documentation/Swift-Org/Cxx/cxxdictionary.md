---
url: "https://docs.swift.org/latest/documentation/cxx/cxxdictionary"
framework: "Swift-Org/Cxx"
---

# CxxDictionary

**Framework**: Swift-Org/Cxx  
**Kind**: protocol  
**Role**: Protocol

A C++ type that represents a dictionary.

## Declaration

```swift
protocol CxxDictionary<Key, Value> : ExpressibleByDictionaryLiteral
```

#### Overview

C++ standard library types such as `std::map` and `std::unordered_map` conform to this protocol.

## Topics

### Associated Types
- [associatedtype Element : CxxPair](./cxxdictionary/element.md)
- [associatedtype InsertionResult](./cxxdictionary/insertionresult.md)
- [associatedtype Key](./cxxdictionary/key.md)
- [associatedtype RawIterator : UnsafeCxxInputIterator](./cxxdictionary/rawiterator.md)
- [associatedtype RawMutableIterator : UnsafeCxxMutableInputIterator](./cxxdictionary/rawmutableiterator.md)
- [associatedtype Size : BinaryInteger](./cxxdictionary/size.md)
- [associatedtype Value](./cxxdictionary/value.md)
### Initializers
- [init()](./cxxdictionary/init%28%29.md)
- [init(Dictionary<Key, Value>)](./cxxdictionary/init%28_%29.md)
  Creates a C++ map containing the elements of a Swift Dictionary.
- [init<S>(grouping: S, by: (S.Element) throws -> Key) rethrows](./cxxdictionary/init%28grouping,by%29.md)
### Instance Methods
- [func compactMapValues<E>((Value) throws(E) -> Value?) throws(E) -> Self](./cxxdictionary/compactmapvalues%28_%29-218g4.md)
- [func compactMapValues<R, E>((Value) throws(E) -> R.Value?) throws(E) -> R](./cxxdictionary/compactmapvalues%28_%29-9wz36.md)
- [func erase(Key) -> Size](./cxxdictionary/erase%28_%29.md)
  Do not implement this function manually in Swift.
- [func filter((_ key: Key, _ value: Value) throws -> Bool) rethrows -> Self](./cxxdictionary/filter%28_%29.md)
- [func mapValues<R, E>((Value) throws(E) -> R.Value) throws(E) -> R](./cxxdictionary/mapvalues%28_%29-46s22.md)
- [func mapValues<E>((Value) throws(E) -> Value) throws(E) -> Self](./cxxdictionary/mapvalues%28_%29-9bek8.md)
- [func merge<E>(Dictionary<Key, Value>, uniquingKeysWith: (Value, Value) throws(E) -> Value) throws(E)](./cxxdictionary/merge%28_,uniquingkeyswith%29-5agb4.md)
- [func merge<T, E>(T, uniquingKeysWith: (Value, Value) throws(E) -> Value) throws(E)](./cxxdictionary/merge%28_,uniquingkeyswith%29-7h62.md)
- [func merge<S, E>(S, uniquingKeysWith: (Value, Value) throws(E) -> Value) throws(E)](./cxxdictionary/merge%28_,uniquingkeyswith%29-885ha.md)
- [func merging<T, E>(T, uniquingKeysWith: (Value, Value) throws(E) -> Value) throws(E) -> Self](./cxxdictionary/merging%28_,uniquingkeyswith%29-2gsmu.md)
- [func merging<S, E>(S, uniquingKeysWith: (Value, Value) throws(E) -> Value) throws(E) -> Self](./cxxdictionary/merging%28_,uniquingkeyswith%29-5ehky.md)
- [func merging<E>(Dictionary<Key, Value>, uniquingKeysWith: (Value, Value) throws(E) -> Value) throws(E) -> Self](./cxxdictionary/merging%28_,uniquingkeyswith%29-6epld.md)
- [func removeValue(forKey: Key) -> Value?](./cxxdictionary/removevalue%28forkey%29.md)
### Subscripts
- [subscript(Key) -> Value?](./cxxdictionary/subscript%28_%29.md)
- [subscript(Key, default _: @autoclosure () -> Value) -> Value](./cxxdictionary/subscript%28_,default%29.md)
### Default Implementations
- [ExpressibleByDictionaryLiteral Implementations](./cxxdictionary/expressiblebydictionaryliteral-implementations.md)

## Relationships

### Inherits From
- [ExpressibleByDictionaryLiteral](https://docs.swift.org/latest/documentation/swift/expressiblebydictionaryliteral)

## See Also

### Collections
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
- [protocol CxxConvertibleToCollection](./cxxconvertibletocollection.md)
  A C++ type that can be converted to a Swift collection.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxdictionary)*