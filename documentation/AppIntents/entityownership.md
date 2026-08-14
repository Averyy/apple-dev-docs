# EntityOwnership

**Framework**: App Intents  
**Kind**: struct

A type that represents the ownership and sharing characteristics of an app entity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct EntityOwnership
```

#### Overview

The [`EntityOwnership`](entityownership.md) structure provides flag-based ownership information. Specify a single state, or combine multiple states using an [`OptionSet`](https://developer.apple.com/documentation/swift/optionset), as shown in the following example:

```swift
// Single ownership and sharing state:
var ownership: EntityOwnership { .shared }

// or

// Combined ownership and sharing states:
var ownership: EntityOwnership { [.shared, .public] }
```

## Topics

### Scoping entity ownership and sharing
- [static let `public`: EntityOwnership](entityownership/public.md)
  A state that indicates the entity represents data a person shares publicly.
- [static let shared: EntityOwnership](entityownership/shared.md)
  A state that indicates a person shares the entity with specific collaborators.
- [static let unknown: EntityOwnership](entityownership/unknown.md)
  A state that indicates that entity ownership or sharing status is unknown or unspecified.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityownership)*