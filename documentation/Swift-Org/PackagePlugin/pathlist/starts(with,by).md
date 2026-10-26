---
url: "https://docs.swift.org/latest/documentation/packageplugin/pathlist/starts(with:by:)"
framework: "Swift-Org/PackagePlugin"
---

# starts(with:by:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: method  
**Role**: Instance Method

Inherited from `Sequence.starts(with:by:)`.

## Declaration

```swift
func starts<PossiblePrefix>(with possiblePrefix: PossiblePrefix, by areEquivalent: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool where PossiblePrefix : Sequence
```


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/pathlist/starts(with:by:))*