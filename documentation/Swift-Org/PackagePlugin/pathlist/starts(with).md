---
url: "https://docs.swift.org/latest/documentation/packageplugin/pathlist/starts(with:)"
framework: "Swift-Org/PackagePlugin"
---

# starts(with:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: method  
**Role**: Instance Method

Inherited from `Sequence.starts(with:)`.

## Declaration

```swift
func starts<PossiblePrefix>(with possiblePrefix: PossiblePrefix) -> Bool where PossiblePrefix : Sequence, Self.Element == PossiblePrefix.Element
```

Available when `Element` conforms to `Equatable`.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/pathlist/starts(with:))*