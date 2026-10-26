# PropertyListSerialization.MutabilityOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSPropertyListMutabilityOptions : NSUInteger;
```

## Topics

### Constants
- [static var mutableContainers: PropertyListSerialization.MutabilityOptions](./mutabilityoptions/mutablecontainers.md)
  Causes the returned property list to have mutable containers but immutable leaves.
- [static var mutableContainersAndLeaves: PropertyListSerialization.MutabilityOptions](./mutabilityoptions/mutablecontainersandleaves.md)
  Causes the returned property list to have mutable containers and leaves.
- [NSPropertyListImmutable](../nspropertylistmutabilityoptions/nspropertylistimmutable.md)
  Causes the returned property list to contain immutable objects.
### Initializers
- [init(rawValue: UInt)](./mutabilityoptions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Constants
- [PropertyListSerialization.PropertyListFormat](./propertylistformat.md)
  These constants are used to specify a property list serialization format.
- [PropertyListSerialization.ReadOptions](./readoptions.md)
  The only read options supported are described in [`PropertyListSerialization.MutabilityOptions`](./mutabilityoptions.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/propertylistserialization/mutabilityoptions)*