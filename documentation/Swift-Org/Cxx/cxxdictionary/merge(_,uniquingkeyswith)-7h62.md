---
url: "https://docs.swift.org/latest/documentation/cxx/cxxdictionary/merge(_:uniquingkeyswith:)-7h62"
framework: "Swift-Org/Cxx"
---

# merge(_:uniquingKeysWith:)

**Framework**: Swift-Org/Cxx  
**Kind**: method  
**Role**: Instance Method

## Declaration

```swift
mutating func merge<T, E>(_ other: T, uniquingKeysWith combine: (Value, Value) throws(E) -> Value) throws(E) where T : CxxDictionary, E : Error, Self.Key == T.Key, Self.Value == T.Value
```


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxdictionary/merge(_:uniquingkeyswith:)-7h62)*