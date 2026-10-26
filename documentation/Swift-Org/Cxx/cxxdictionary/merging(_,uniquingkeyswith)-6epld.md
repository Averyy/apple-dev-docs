---
url: "https://docs.swift.org/latest/documentation/cxx/cxxdictionary/merging(_:uniquingkeyswith:)-6epld"
framework: "Swift-Org/Cxx"
---

# merging(_:uniquingKeysWith:)

**Framework**: Swift-Org/Cxx  
**Kind**: method  
**Role**: Instance Method

## Declaration

```swift
func merging<E>(_ other: Dictionary<Key, Value>, uniquingKeysWith combine: (Value, Value) throws(E) -> Value) throws(E) -> Self where E : Error, Self.Key : Hashable
```


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxdictionary/merging(_:uniquingkeyswith:)-6epld)*