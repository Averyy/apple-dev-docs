# CFPropertyListMutabilityOptions

**Framework**: Core Foundation  
**Kind**: struct  
**Role**: Structure

Type for flags that determine the degree of mutability of newly created property lists.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct CFPropertyListMutabilityOptions
```

```c
enum CFPropertyListMutabilityOptions : CFOptionFlags;
```

#### Overview

See [Property List Mutability Options](./property_list_mutability_options.md) for possible values.

## Topics

### Initializers
- [init(rawValue: CFOptionFlags)](./cfpropertylistmutabilityoptions/init%28rawvalue%29.md)
### Type Properties
- [static var mutableContainers: CFPropertyListMutabilityOptions](./cfpropertylistmutabilityoptions/mutablecontainers.md)
  Specifies that the property list should have mutable containers but immutable leaves.
- [static var mutableContainersAndLeaves: CFPropertyListMutabilityOptions](./cfpropertylistmutabilityoptions/mutablecontainersandleaves.md)
  Specifies that the property list should have mutable containers and mutable leaves.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfpropertylistmutabilityoptions)*