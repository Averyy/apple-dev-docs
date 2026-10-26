---
url: "https://docs.swift.org/latest/documentation/cxx/cxxdictionary/merge(_:uniquingkeyswith:)-885ha"
framework: "Swift-Org/Cxx"
---

# merge(_:uniquingKeysWith:)

**Framework**: Swift-Org/Cxx  
**Kind**: method  
**Role**: Instance Method

## Declaration

```swift
mutating func merge<S, E>(_ other: S, uniquingKeysWith combine: (Value, Value) throws(E) -> Value) throws(E) where S : Sequence, E : Error, S.Element == (Self.Key, Self.Value)
```


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxdictionary/merge(_:uniquingkeyswith:)-885ha)*