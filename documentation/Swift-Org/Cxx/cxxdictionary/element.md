---
url: "https://docs.swift.org/latest/documentation/cxx/cxxdictionary/element"
framework: "Swift-Org/Cxx"
---

# Element

**Framework**: Swift-Org/Cxx  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

## Declaration

```swift
associatedtype Element : CxxPair where Self.Element == Self.RawIterator.Pointee, Self.Key == Self.Element.First, Self.Value == Self.Element.Second
```


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxdictionary/element)*