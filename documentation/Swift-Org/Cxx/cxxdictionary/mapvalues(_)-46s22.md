---
url: "https://docs.swift.org/latest/documentation/cxx/cxxdictionary/mapvalues(_:)-46s22"
framework: "Swift-Org/Cxx"
---

# mapValues(_:)

**Framework**: Swift-Org/Cxx  
**Kind**: method  
**Role**: Instance Method

## Declaration

```swift
func mapValues<R, E>(_ transform: (Value) throws(E) -> R.Value) throws(E) -> R where R : CxxDictionary, E : Error, Self.Key == R.Key
```


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxdictionary/mapvalues(_:)-46s22)*