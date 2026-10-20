# ManagedAppDistributionError

**Framework**: ManagedAppDistribution  
**Kind**: enum  
**Role**: Enumeration

Codes that identify errors in Managed App Distribution.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 2.4+

## Declaration

```swift
enum ManagedAppDistributionError
```

## Topics

### Inspecting errors
- [ManagedAppDistributionError.deviceNotManaged](./managedappdistributionerror/devicenotmanaged.md)
  An error that indicates this device isn’t managed.
- [ManagedAppDistributionError.networkError](./managedappdistributionerror/networkerror.md)
  An error that indicates a network issue.
- [ManagedAppDistributionError.unrecoverableError](./managedappdistributionerror/unrecoverableerror.md)
  An error that is unspecified and unrecoverable.
- [ManagedAppDistributionError.unsupportedPlatform](./managedappdistributionerror/unsupportedplatform.md)
  An error that indicates the platform is unsupported.
### Providing error information
- [var description: String](./managedappdistributionerror/description.md)
  A localized description of the error.
- [var errorDescription: String?](./managedappdistributionerror/errordescription.md)
  A brief description of the error.
- [var failureReason: String?](./managedappdistributionerror/failurereason.md)
  A detailed description of the error.
- [var recoveryOptions: [String]](./managedappdistributionerror/recoveryoptions.md)
  A set of possible recovery options to present.
- [var recoverySuggestion: String?](./managedappdistributionerror/recoverysuggestion.md)
  A suggestion for recovering from the error.
- [var localizedStringResource: LocalizedStringResource](./managedappdistributionerror/localizedstringresource.md)
  A set of localized error strings.
### Providing help information
- [var helpAnchor: String?](./managedappdistributionerror/helpanchor.md)
  A link to help documentation.
### Recovering from errors
- [func attemptRecovery(optionIndex: Int) -> Bool](./managedappdistributionerror/attemptrecovery%28optionindex%29.md)
  Attempt to recover from this error when someone selects the option at the given index.
- [func attemptRecovery(optionIndex: Int, resultHandler: (Bool) -> Void)](./managedappdistributionerror/attemptrecovery%28optionindex,resulthandler%29.md)
  Attempt to recover from this error when someone selects the option at the given index.
### Enumeration Cases
- [ManagedAppDistributionError.appNotManaged](./managedappdistributionerror/appnotmanaged.md)
  An error that indicates that the calling app is not managed
- [ManagedAppDistributionError.licenseNotFound](./managedappdistributionerror/licensenotfound.md)
  An error that indicates that a license wasn’t found for requested app.

## Relationships

### Conforms To
- [CustomLocalizedStringResourceConvertible](../Foundation/customlocalizedstringresourceconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Error](../Swift/error.md)
- [Hashable](../Swift/hashable.md)
- [LocalizedError](../Foundation/localizederror.md)
- [RecoverableError](../Foundation/recoverableerror.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappdistributionerror)*