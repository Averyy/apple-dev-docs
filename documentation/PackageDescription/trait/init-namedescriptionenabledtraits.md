# init(name:description:enabledTraits:)

**Framework**: PackageDescription  
**Kind**: init

Initializes a new trait.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
init(name: String, description: String? = nil, enabledTraits: Set<String> = [])
```

## Parameters

- `name`: The trait’s canonical name.
- `description`: The trait’s description.
- `enabledTraits`: A set of other traits of this package that this trait enables.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/trait/init(name:description:enabledtraits:))*