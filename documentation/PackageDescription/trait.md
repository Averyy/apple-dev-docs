# Trait

**Framework**: PackageDescription  
**Kind**: struct

A struct representing a package’s trait.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
struct Trait
```

#### Overview

Traits can be used for expressing conditional compilation and optional dependencies.

> ❗ **Important**: Traits must be strictly additive and enabling a trait  remove API.

## Topics

### Initializers
- [init(name: String, description: String?, enabledTraits: Set<String>)](trait/init(name:description:enabledtraits:).md)
  Initializes a new trait.
### Instance Properties
- [var description: String?](trait/description.md)
  The trait’s description.
- [var enabledTraits: Set<String>](trait/enabledtraits.md)
  A set of other traits of this package that this trait enables.
- [var name: String](trait/name.md)
  The trait’s canonical name.
### Type Methods
- [static func `default`(enabledTraits: Set<String>) -> Trait](trait/default(enabledtraits:).md)
  Declares the default traits for this package.
- [static func trait(name: String, description: String?, enabledTraits: Set<String>) -> Trait](trait/trait(name:description:enabledtraits:).md)
  Initializes a new trait.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var traits: Set<Trait>](package/traits.md)
  The set of traits of this package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/trait)*