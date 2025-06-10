# ManagedAppConfigurationDecodingError

**Framework**: ManagedApp  
**Kind**: protocol

A protocol for an error that describes an issue with decoding the configuration.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- visionOS 2.4+

## Declaration

```swift
protocol ManagedAppConfigurationDecodingError : Decodable, Encodable, Error
```

## Mentions

- [Specifying and decoding a configuration](specifying-and-decoding-a-configuration.md)

#### Overview

For more information, see [`configurations(_:)`](managedappconfigurationprovider/configurations(_:).md).

## Topics

### Identifying an error
- [var code: ManagedAppConfigurationDecodingErrorCode](managedappconfigurationdecodingerror/code.md)
  An app-specific error code that identifies a configuration issue.
### Interpreting an error
- [var message: String](managedappconfigurationdecodingerror/message.md)
  A human-readable message that describes the configuration issue.

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Error](../Swift/Error.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum ManagedAppError](managedapperror.md)
  Errors that functions in the ManagedApp framework can throw.
- [struct ManagedAppConfigurationDecodingErrorCode](managedappconfigurationdecodingerrorcode.md)
  A code for an error that occurs during configuration decoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedapp/managedappconfigurationdecodingerror)*