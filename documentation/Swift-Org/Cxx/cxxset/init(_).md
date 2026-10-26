---
url: "https://docs.swift.org/latest/documentation/cxx/cxxset/init(_:)"
framework: "Swift-Org/Cxx"
---

# init(_:)

**Framework**: Swift-Org/Cxx  
**Kind**: init  
**Role**: Initializer

Creates a C++ set containing the elements of a Swift Sequence.

## Declaration

```swift
init<S>(_ sequence: S) where S : Sequence, Self.Element == S.Element
```

#### Discussion

This initializes the set by copying every element of the sequence.

> **Complexity**: O(*n*), where *n* is the number of elements in the Swift sequence


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxset/init(_:))*