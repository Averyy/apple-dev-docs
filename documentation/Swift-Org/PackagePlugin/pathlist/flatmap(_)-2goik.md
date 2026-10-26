---
url: "https://docs.swift.org/latest/documentation/packageplugin/pathlist/flatmap(_:)-2goik"
framework: "Swift-Org/PackagePlugin"
---

# flatMap(_:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: method  
**Role**: Instance Method

Inherited from `Sequence.flatMap(_:)`.

**Availability**:
- Swift - Deprecated in 4.1 (renamed: compactMap(_:))

> **Deprecated**: Please use compactMap(_:) for the case where closure returns an optional value

## Declaration

```swift
func flatMap<ElementOfResult>(_ transform: (Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]
```


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/pathlist/flatmap(_:)-2goik)*