---
url: "https://docs.swift.org/latest/documentation/cxx/cxxdictionary/compactmapvalues(_:)-9wz36"
framework: "Swift-Org/Cxx"
---

# compactMapValues(_:)

**Framework**: Swift-Org/Cxx  
**Kind**: method  
**Role**: Instance Method

## Declaration

```swift
func compactMapValues<R, E>(_ transform: (Value) throws(E) -> R.Value?) throws(E) -> R where R : CxxDictionary, E : Error, Self.Key == R.Key
```


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxdictionary/compactmapvalues(_:)-9wz36)*