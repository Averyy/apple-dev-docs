---
url: "https://docs.swift.org/latest/documentation/cxx/cxxdictionary/merging(_:uniquingkeyswith:)-5ehky"
framework: "Swift-Org/Cxx"
---

# merging(_:uniquingKeysWith:)

**Framework**: Swift-Org/Cxx  
**Kind**: method  
**Role**: Instance Method

## Declaration

```swift
func merging<S, E>(_ other: S, uniquingKeysWith combine: (Value, Value) throws(E) -> Value) throws(E) -> Self where S : Sequence, E : Error, S.Element == (Self.Key, Self.Value)
```


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxdictionary/merging(_:uniquingkeyswith:)-5ehky)*