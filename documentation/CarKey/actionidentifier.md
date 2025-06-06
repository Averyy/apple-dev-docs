# ActionIdentifier

**Framework**: CarKey  
**Kind**: struct

A type that stores the designation code for one of the actions that a vehicle feature supports.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.3+
- watchOS 9.0+

## Declaration

```swift
struct ActionIdentifier
```

#### Overview

An [`ActionIdentifier`](actionidentifier.md) type wraps a vehicle-specific code you define. This code — known as the action identifier — corresponds to an action your vehicle can take for a particular feature. For example, you might define actions to lock or unlock the vehicle’s doors. Use this type in conjunction with a specific [`FunctionIdentifier`](functionidentifier.md) type to specify the complete action you want to perform on a vehicle.

## Topics

### Creating the Action Identifier
- [init(rawValue: Int)](actionidentifier/init(rawvalue:).md)
  Creates and returns a new action identifier with the specified value.
- [init(Int)](actionidentifier/init(_:).md)
  Creates and returns a new action identifier with the specified value.
### Getting the Value
- [let rawValue: Int](actionidentifier/rawvalue-swift.property.md)
  The raw value that corresponds to the feature-specific action.
### Type Aliases
- [ActionIdentifier.RawValue](actionidentifier/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](actionidentifier/equatable-implementations.md)
- [RawRepresentable Implementations](actionidentifier/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [struct RemoteKeylessEntryAction](remotekeylessentryaction.md)
  An automatically ending action that you want to perform on a vehicle.
- [struct RemoteKeylessEntryEnduringAction](remotekeylessentryenduringaction.md)
  An action with an optional stopping point that you want to perform on a vehicle.
- [struct FunctionIdentifier](functionidentifier.md)
  A type that stores the designation code for one of your vehicle’s features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/actionidentifier)*