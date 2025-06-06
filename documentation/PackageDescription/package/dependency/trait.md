# Package.Dependency.Trait

**Framework**: PackageDescription  
**Kind**: struct

A struct representing an enabled trait of a dependency.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
struct Trait
```

## Topics

### Structures
- [Package.Dependency.Trait.Condition](package/dependency/trait/condition-swift.struct.md)
  A condition that limits the application of a dependencies trait.
### Operators
- [static func == (Package.Dependency.Trait, Package.Dependency.Trait) -> Bool](package/dependency/trait/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(name: String, condition: Package.Dependency.Trait.Condition?)](package/dependency/trait/init(name:condition:).md)
  Initializes a new enabled trait.
- [init(stringLiteral: StringLiteralType)](package/dependency/trait/init(stringliteral:).md)
  Creates an instance initialized to the given string value.
### Instance Properties
- [var condition: Package.Dependency.Trait.Condition?](package/dependency/trait/condition-swift.property.md)
  The condition under which the trait is enabled.
- [var hashValue: Int](package/dependency/trait/hashvalue.md)
  The hash value.
- [var name: String](package/dependency/trait/name.md)
  The name of the enabled trait.
### Instance Methods
- [func hash(into: inout Hasher)](package/dependency/trait/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [Package.Dependency.Trait.ExtendedGraphemeClusterLiteralType](package/dependency/trait/extendedgraphemeclusterliteraltype.md)
  A type that represents an extended grapheme cluster literal.
- [Package.Dependency.Trait.StringLiteralType](package/dependency/trait/stringliteraltype.md)
  A type that represents a string literal.
- [Package.Dependency.Trait.UnicodeScalarLiteralType](package/dependency/trait/unicodescalarliteraltype.md)
  A type that represents a Unicode scalar literal.
### Type Properties
- [static let defaults: Package.Dependency.Trait](package/dependency/trait/defaults.md)
  Enables all default traits of a package.
### Type Methods
- [static func trait(name: String, condition: Package.Dependency.Trait.Condition?) -> Package.Dependency.Trait](package/dependency/trait/trait(name:condition:).md)
  Initializes a new enabled trait.
### Default Implementations
- [Equatable Implementations](package/dependency/trait/equatable-implementations.md)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](package/dependency/trait/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringLiteral Implementations](package/dependency/trait/expressiblebystringliteral-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/trait)*