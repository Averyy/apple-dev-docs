---
url: "https://docs.swift.org/latest/documentation/cxx/cxxiterable/rawiterator"
framework: "Swift-Org/Cxx"
---

# RawIterator

**Framework**: Swift-Org/Cxx  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

## Declaration

```swift
associatedtype RawIterator : UnsafeCxxInputIterator where Self.RawIterator.DereferenceResult : _Pointer, Self.RawIterator.Pointee == Self.RawIterator.DereferenceResult.Pointee
```


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxiterable/rawiterator)*