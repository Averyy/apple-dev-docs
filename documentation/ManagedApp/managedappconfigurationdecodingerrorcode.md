# ManagedAppConfigurationDecodingErrorCode

**Framework**: ManagedApp  
**Kind**: struct

A code for an error that occurs during configuration decoding.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- visionOS 2.4+

## Declaration

```swift
struct ManagedAppConfigurationDecodingErrorCode
```

## Mentions

- [Specifying and decoding a configuration](specifying-and-decoding-a-configuration.md)

#### Overview

The system reserves some codes for its use only. Reserved codes are equal to or greater than `firstReserved`. Codes less than the `firstReserved` value are app-specific. For more information, see [`code`](managedappconfigurationdecodingerror/code.md).

## Topics

### Initializing an error
- [init?(rawValue: Int)](managedappconfigurationdecodingerrorcode/init(rawvalue:).md)
  Initializes a configuration decoding error code.
### Identifying an error
- [let rawValue: Int](managedappconfigurationdecodingerrorcode/rawvalue-swift.property.md)
  The error code’s value in its underlying type.
### Type Aliases
- [ManagedAppConfigurationDecodingErrorCode.RawValue](managedappconfigurationdecodingerrorcode/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static let dataCorrupted: Int](managedappconfigurationdecodingerrorcode/datacorrupted.md)
  An error code that indicates the decoder encountered corrupt data.
- [static let firstReserved: Int](managedappconfigurationdecodingerrorcode/firstreserved.md)
  An error code for the start of the range of reserved error codes.
- [static let generic: Int](managedappconfigurationdecodingerrorcode/generic.md)
  A reserved error that indicates the decoder threw an unknown custom error.
- [static let keyNotFound: Int](managedappconfigurationdecodingerrorcode/keynotfound.md)
  An error code that indicates the decoder encountered an unknown coding key.
- [static let timeout: Int](managedappconfigurationdecodingerrorcode/timeout.md)
  An error code that indicates the decoder timed out.
- [static let typeMismatch: Int](managedappconfigurationdecodingerrorcode/typemismatch.md)
  An error code that indicates the decoder encountered a type mismatch.
- [static let valueNotFound: Int](managedappconfigurationdecodingerrorcode/valuenotfound.md)
  An error code that indicates a coding key yields no value.
### Default Implementations
- [Equatable Implementations](managedappconfigurationdecodingerrorcode/equatable-implementations.md)
- [RawRepresentable Implementations](managedappconfigurationdecodingerrorcode/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum ManagedAppError](managedapperror.md)
  Errors that functions in the ManagedApp framework can throw.
- [protocol ManagedAppConfigurationDecodingError](managedappconfigurationdecodingerror.md)
  A protocol for an error that describes an issue with decoding the configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedapp/managedappconfigurationdecodingerrorcode)*