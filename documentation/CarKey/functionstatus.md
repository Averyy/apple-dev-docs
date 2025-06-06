# FunctionStatus

**Framework**: CarKey  
**Kind**: struct

A value that the vehicle can return to indicate the status of a particular vehicle feature.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.3+
- watchOS 9.0+

## Declaration

```swift
struct FunctionStatus
```

#### Overview

A [`FunctionStatus`](functionstatus.md) type wraps the custom code that the vehicle returns. You define the status codes and their meanings for your vehicle’s features. For example, you might define status codes to represent the locked, unlocked, and unknown states of your vehicle’s door-locking system.

## Topics

### Creating a Function Status Type
- [init(rawValue: Int)](functionstatus/init(rawvalue:).md)
  Creates and returns a new function status with the specified value.
- [init(Int)](functionstatus/init(_:).md)
  Creates and returns a new function status with the specified value.
### Getting the Value
- [let rawValue: Int](functionstatus/rawvalue-swift.property.md)
  The raw value that corresponds to the feature-specific status.
### Type Aliases
- [FunctionStatus.RawValue](functionstatus/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](functionstatus/equatable-implementations.md)
- [RawRepresentable Implementations](functionstatus/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [var supportedFunctions: [FunctionIdentifier]](vehiclereport/supportedfunctions.md)
  An array of function identifiers that indicates the features the vehicle supports, populated only after the first BLE connection with the vehicle.
- [func status(for: FunctionIdentifier) throws -> FunctionStatus?](vehiclereport/status(for:).md)
  Returns the current status of the specified vehicle function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/functionstatus)*