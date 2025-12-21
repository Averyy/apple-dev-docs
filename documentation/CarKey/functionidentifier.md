# FunctionIdentifier

**Framework**: CarKey  
**Kind**: struct

A type that stores the designation code for one of your vehicle’s features.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.3+
- watchOS 9.0+

## Declaration

```swift
struct FunctionIdentifier
```

#### Overview

A [`FunctionIdentifier`](functionidentifier.md) type wraps a vehicle-specific code you define. This code — known as the function identifier — corresponds to a particular feature of your vehicle. For example, one function identifier might represent the vehicle’s door locks and another represent the vehicle’s window system. Use this type in conjunction with an [`ActionIdentifier`](actionidentifier.md) type to specify the complete action you want to perform on a vehicle.

## Topics

### Creating a Function Identifier
- [init(rawValue: Int)](functionidentifier/init(rawvalue:).md)
  Creates and returns a new function identifier with the specified value.
- [init(Int)](functionidentifier/init(_:).md)
  Creates and returns a new function identifier with the specified value.
### Getting the Value
- [let rawValue: Int](functionidentifier/rawvalue.md)
  The raw value that corresponds to the specific feature of your vehicle.

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
- [struct ActionIdentifier](actionidentifier.md)
  A type that stores the designation code for one of the actions that a vehicle feature supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/functionidentifier)*