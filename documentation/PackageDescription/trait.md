# Trait

**Framework**: PackageDescription  
**Kind**: struct

A package trait.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
struct Trait
```

#### Overview

A trait is a package feature that expresses conditional compilation and potentially optional dependencies. It is typically used to expose additional or extended API for the package.

When you define a trait on a package, the package manager uses the name of that trait as a conditional block for the package’s code. Use the conditional block to enable imports or code paths for that trait. For example, a trait with the canonical name `MyTrait` allows you to use the name as a conditional block:

```swift
#if MyTrait
// additional imports or APIs that MyTrait enables
#endif // MyTrait
```

> ❗ **Important**: Traits must be strictly additive. Enabling a trait **must not** remove API.

If your conditional code requires a dependency that you want to enable only when the trait is enabled, add a conditional declaration to the target dependencies, then include the import statement within the conditional block. The following example illustrates enabling the dependency `MyDependency` when the trait `Trait1` is enabled:

```swift
targets: [
   .target(
       name: "MyTarget",
       dependencies: [
           .product(
               name: "MyAPI",
               package: "MyDependency",
               condition: .when(traits: ["Trait1"])
           )
       ]
   ),
]
```

Coordinate a declaration like the example above with code that imports the dependency in a conditional block:

```swift
#if Trait1
import MyAPI
#endif // Trait1
```

## Topics

### Initializers
- [init(name: String, description: String?, enabledTraits: Set<String>)](trait/init(name:description:enabledtraits:).md)
  Creates a trait with a name, a description, and set of additional traits it enables.
- [init(stringLiteral: StringLiteralType)](trait/init(stringliteral:).md)
  Creates a trait with the name you provide.
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
  Creates a trait with a name, a description, and set of additional traits it enables.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var traits: Set<Trait>](package/traits.md)
  The set of traits this package provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/trait)*