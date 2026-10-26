---
url: "https://docs.swift.org/latest/documentation/packageplugin/filelist/elementsequal(_:by:)"
framework: "Swift-Org/PackagePlugin"
---

# elementsEqual(_:by:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: method  
**Role**: Instance Method

Inherited from `Sequence.elementsEqual(_:by:)`.

## Declaration

```swift
func elementsEqual<OtherSequence>(_ other: OtherSequence, by areEquivalent: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool where OtherSequence : Sequence
```


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/filelist/elementsequal(_:by:))*