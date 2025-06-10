# CFPropertyListMutabilityOptions

**Framework**: Core Foundation  
**Kind**: struct

Type for flags that determine the degree of mutability of newly created property lists.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct CFPropertyListMutabilityOptions
```

#### Overview

See [`Property List Mutability Options`](property_list_mutability_options.md) for possible values.

## Topics

### Initializers
- [init(rawValue: CFOptionFlags)](cfpropertylistmutabilityoptions/init(rawvalue:).md)
### Type Properties
- [static var mutableContainers: CFPropertyListMutabilityOptions](cfpropertylistmutabilityoptions/mutablecontainers.md)
  Specifies that the property list should have mutable containers but immutable leaves.
- [static var mutableContainersAndLeaves: CFPropertyListMutabilityOptions](cfpropertylistmutabilityoptions/mutablecontainersandleaves.md)
  Specifies that the property list should have mutable containers and mutable leaves.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpropertylistmutabilityoptions)*