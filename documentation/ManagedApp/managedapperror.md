# ManagedAppError

**Framework**: ManagedApp  
**Kind**: enum

Errors that functions in the ManagedApp framework can throw.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- macOS 27.0+ (Beta)
- visionOS 2.4+

## Declaration

```swift
enum ManagedAppError
```

## Topics

### Interpreting an error
- [ManagedAppError.invalidIdentifier](managedapperror/invalididentifier.md)
  An error that indicates a failure finding an identifier.
### Enumeration Cases
- [ManagedAppError.internalError](managedapperror/internalerror.md)
  An error that indicates a failure at the system level.
- [ManagedAppError.serverError](managedapperror/servererror.md)
  An error that indicates a failure requesting a secret from the asset server.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Error](../swift/error.md)
- [Hashable](../swift/hashable.md)
- [LocalizedError](../foundation/localizederror.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol ManagedAppConfigurationDecodingError](managedappconfigurationdecodingerror.md)
  A protocol for an error that describes an issue with decoding the configuration.
- [struct ManagedAppConfigurationDecodingErrorCode](managedappconfigurationdecodingerrorcode.md)
  A code for an error that occurs during configuration decoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedapp/managedapperror)*