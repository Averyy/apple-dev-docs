# Package.Dependency.Trait.Condition

**Framework**: PackageDescription  
**Kind**: struct

A condition that limits the application of a dependencies trait.

**Availability**:
- SwiftPM 6.1+

## Declaration

```swift
struct Condition
```

## Topics

### Operators
- [static func == (Package.Dependency.Trait.Condition, Package.Dependency.Trait.Condition) -> Bool](package/dependency/trait/condition-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](package/dependency/trait/condition-swift.struct/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](package/dependency/trait/condition-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Methods
- [static func when(traits: Set<String>) -> Package.Dependency.Trait.Condition?](package/dependency/trait/condition-swift.struct/when(traits:).md)
  Creates a package dependency trait condition.
### Default Implementations
- [Equatable Implementations](package/dependency/trait/condition-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/dependency/trait/condition-swift.struct)*