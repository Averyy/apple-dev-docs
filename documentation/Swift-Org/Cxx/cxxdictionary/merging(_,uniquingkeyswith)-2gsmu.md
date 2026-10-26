---
url: "https://docs.swift.org/latest/documentation/cxx/cxxdictionary/merging(_:uniquingkeyswith:)-2gsmu"
framework: "Swift-Org/Cxx"
---

# merging(_:uniquingKeysWith:)

**Framework**: Swift-Org/Cxx  
**Kind**: method  
**Role**: Instance Method

## Declaration

```swift
func merging<T, E>(_ other: T, uniquingKeysWith combine: (Value, Value) throws(E) -> Value) throws(E) -> Self where T : CxxDictionary, E : Error, Self.Key == T.Key, Self.Value == T.Value
```


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxdictionary/merging(_:uniquingkeyswith:)-2gsmu)*