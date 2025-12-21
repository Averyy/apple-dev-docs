# PropertyListSerialization.MutabilityOptions

**Framework**: Foundation  
**Kind**: struct

These constants specify mutability options in property lists.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct MutabilityOptions
```

## Topics

### Constants
- [static var mutableContainers: PropertyListSerialization.MutabilityOptions](propertylistserialization/mutabilityoptions/mutablecontainers.md)
  Causes the returned property list to have mutable containers but immutable leaves.
- [static var mutableContainersAndLeaves: PropertyListSerialization.MutabilityOptions](propertylistserialization/mutabilityoptions/mutablecontainersandleaves.md)
  Causes the returned property list to have mutable containers and leaves.
### Initializers
- [init(rawValue: UInt)](propertylistserialization/mutabilityoptions/init(rawvalue:).md)

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

## See Also

- [PropertyListSerialization.PropertyListFormat](propertylistserialization/propertylistformat.md)
  These constants are used to specify a property list serialization format.
- [PropertyListSerialization.ReadOptions](propertylistserialization/readoptions.md)
  The only read options supported are described in [`PropertyListSerialization.MutabilityOptions`](propertylistserialization/mutabilityoptions.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/propertylistserialization/mutabilityoptions)*