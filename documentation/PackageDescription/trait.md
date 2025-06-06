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

Traits must be strictly additive and enabling a trait  remove API.

## Topics

### Operators
- [static func == (Trait, Trait) -> Bool](trait/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(name: String, description: String?, enabledTraits: Set<String>)](trait/init(name:description:enabledtraits:).md)
  Initializes a new trait.
- [init(stringLiteral: StringLiteralType)](trait/init(stringliteral:).md)
  Creates an instance initialized to the given string value.
### Instance Properties
- [var description: String?](trait/description.md)
  The trait’s description.
- [var enabledTraits: Set<String>](trait/enabledtraits.md)
  A set of other traits of this package that this trait enables.
- [var hashValue: Int](trait/hashvalue.md)
  The hash value.
- [var name: String](trait/name.md)
  The trait’s canonical name.
### Instance Methods
- [func hash(into: inout Hasher)](trait/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [typealias ExtendedGraphemeClusterLiteralType](trait/extendedgraphemeclusterliteraltype.md)
  A type that represents an extended grapheme cluster literal.
- [typealias StringLiteralType](trait/stringliteraltype.md)
  A type that represents a string literal.
- [typealias UnicodeScalarLiteralType](trait/unicodescalarliteraltype.md)
  A type that represents a Unicode scalar literal.
### Type Methods
- [static func `default`(enabledTraits: Set<String>) -> Trait](trait/default(enabledtraits:).md)
  Declares the default traits for this package.
- [static func trait(name: String, description: String?, enabledTraits: Set<String>) -> Trait](trait/trait(name:description:enabledtraits:).md)
  Initializes a new trait.
### Default Implementations
- [Equatable Implementations](trait/equatable-implementations.md)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](trait/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringLiteral Implementations](trait/expressiblebystringliteral-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/trait)*