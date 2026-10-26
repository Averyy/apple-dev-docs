---
url: "https://docs.swift.org/latest/documentation/cxx/cxxborrowingiterator"
framework: "Swift-Org/Cxx"
---

# CxxBorrowingIterator

**Framework**: Swift-Org/Cxx  
**Kind**: struct  
**Role**: Structure

## Declaration

```swift
@frozen
struct CxxBorrowingIterator<T> where T : CxxIterable, T : ~Copyable, T : ~Escapable, T.Element : ~Copyable
```

## Topics

### Initializers
- [init(begin: T.RawIterator, end: T.RawIterator, sequence: borrowing T)](./cxxborrowingiterator/init%28begin,end,sequence%29.md)
### Instance Properties
- [var count: Int](./cxxborrowingiterator/count.md)
### Instance Methods
- [func nextSpan() -> Span<Element>](./cxxborrowingiterator/nextspan%28%29.md)
- [func nextSpan(maxCount: Int) -> Span<Element>](./cxxborrowingiterator/nextspan%28maxcount%29-9yg0c.md)
### Default Implementations
- [BorrowingIteratorProtocol Implementations](./cxxborrowingiterator/borrowingiteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [BorrowingIteratorProtocol](https://docs.swift.org/latest/documentation/swift/borrowingiteratorprotocol)


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxborrowingiterator)*