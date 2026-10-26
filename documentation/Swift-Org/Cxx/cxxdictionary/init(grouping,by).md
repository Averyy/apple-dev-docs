---
url: "https://docs.swift.org/latest/documentation/cxx/cxxdictionary/init(grouping:by:)"
framework: "Swift-Org/Cxx"
---

# init(grouping:by:)

**Framework**: Swift-Org/Cxx  
**Kind**: init  
**Role**: Initializer

## Declaration

```swift
init<S>(grouping values: S, by keyForValue: (S.Element) throws -> Key) rethrows where S : Sequence, Self.Value : CxxVector, S.Element == Self.Value.Element
```


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxdictionary/init(grouping:by:))*