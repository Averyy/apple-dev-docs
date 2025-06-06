# trait(name:description:enabledTraits:)

**Framework**: PackageDescription  
**Kind**: method

Initializes a new trait.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
static func trait(name: String, description: String? = nil, enabledTraits: Set<String> = []) -> Trait
```

## Parameters

- `name`: The trait’s canonical name.
- `description`: The trait’s description.
- `enabledTraits`: A set of other traits of this package that this trait enables.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/trait/trait(name:description:enabledtraits:))*