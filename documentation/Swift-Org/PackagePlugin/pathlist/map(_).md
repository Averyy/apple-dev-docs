---
url: "https://docs.swift.org/latest/documentation/packageplugin/pathlist/map(_:)"
framework: "Swift-Org/PackagePlugin"
---

# map(_:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: method  
**Role**: Instance Method

Inherited from `Sequence.map(_:)`.

## Declaration

```swift
func map<T, E>(_ transform: (Self.Element) throws(E) -> T) throws(E) -> [T] where E : Error
```


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/pathlist/map(_:))*