---
url: "https://docs.swift.org/latest/documentation/cxx/cxxdictionary/merge(_:uniquingkeyswith:)-5agb4"
framework: "Swift-Org/Cxx"
---

# merge(_:uniquingKeysWith:)

**Framework**: Swift-Org/Cxx  
**Kind**: method  
**Role**: Instance Method

## Declaration

```swift
mutating func merge<E>(_ other: Dictionary<Key, Value>, uniquingKeysWith combine: (Value, Value) throws(E) -> Value) throws(E) where E : Error, Self.Key : Hashable
```


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxdictionary/merge(_:uniquingkeyswith:)-5agb4)*