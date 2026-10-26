---
url: "https://docs.swift.org/latest/documentation/packageplugin/pathlist/elementsequal(_:)"
framework: "Swift-Org/PackagePlugin"
---

# elementsEqual(_:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: method  
**Role**: Instance Method

Inherited from `Sequence.elementsEqual(_:)`.

## Declaration

```swift
func elementsEqual<OtherSequence>(_ other: OtherSequence) -> Bool where OtherSequence : Sequence, Self.Element == OtherSequence.Element
```

Available when `Element` conforms to `Equatable`.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/pathlist/elementsequal(_:))*