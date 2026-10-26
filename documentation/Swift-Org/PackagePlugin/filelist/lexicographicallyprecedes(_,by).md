---
url: "https://docs.swift.org/latest/documentation/packageplugin/filelist/lexicographicallyprecedes(_:by:)"
framework: "Swift-Org/PackagePlugin"
---

# lexicographicallyPrecedes(_:by:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: method  
**Role**: Instance Method

Inherited from `Sequence.lexicographicallyPrecedes(_:by:)`.

## Declaration

```swift
func lexicographicallyPrecedes<OtherSequence>(_ other: OtherSequence, by areInIncreasingOrder: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool where OtherSequence : Sequence, Self.Element == OtherSequence.Element
```


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/filelist/lexicographicallyprecedes(_:by:))*