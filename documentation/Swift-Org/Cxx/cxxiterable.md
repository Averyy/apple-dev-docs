---
url: "https://docs.swift.org/latest/documentation/cxx/cxxiterable"
framework: "Swift-Org/Cxx"
---

# CxxIterable

**Framework**: Swift-Org/Cxx  
**Kind**: protocol  
**Role**: Protocol

Use this protocol to conform custom C++ sequence types to Swift’s `Iterable` protocol like this:

## Declaration

```swift
protocol CxxIterable<Element> : Iterable, ~Copyable, ~Escapable where Self.Failure == Never
```

#### Overview

```swift
extension MyCxxSequenceType : CxxIterable {}
```

This requires the C++ sequence type to define const methods `begin()` and `end()` which return input iterators into the C++ sequence. The iterator types must conform to `UnsafeCxxInputIterator`.

## Topics

### Associated Types
- [associatedtype BorrowingIterator : ~Copyable, ~Escapable = CxxBorrowingIterator<Self>](./cxxiterable/borrowingiterator.md)
- [associatedtype Element : ~Copyable](./cxxiterable/element.md)
- [associatedtype RawIterator : UnsafeCxxInputIterator](./cxxiterable/rawiterator.md)

## Relationships

### Inherits From
- [Iterable](https://docs.swift.org/latest/documentation/swift/iterable)


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxiterable)*