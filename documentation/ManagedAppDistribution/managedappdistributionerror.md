# ManagedAppDistributionError

**Framework**: ManagedAppDistribution  
**Kind**: enum

Codes that identify errors in Managed App Distribution.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- visionOS 2.4+

## Declaration

```swift
enum ManagedAppDistributionError
```

## Topics

### Creating an error object
- [init(from: any Decoder) throws](managedappdistributionerror/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Inspecting errors
- [ManagedAppDistributionError.deviceNotManaged](managedappdistributionerror/devicenotmanaged.md)
  An error that indicates this device isn’t managed.
- [ManagedAppDistributionError.networkError](managedappdistributionerror/networkerror.md)
  An error that indicates a network issue.
- [ManagedAppDistributionError.unrecoverableError](managedappdistributionerror/unrecoverableerror.md)
  An error that is unspecified and unrecoverable.
- [ManagedAppDistributionError.unsupportedPlatform](managedappdistributionerror/unsupportedplatform.md)
  An error that indicates the platform is unsupported.
### Providing error information
- [var description: String](managedappdistributionerror/description.md)
  A localized description of the error.
- [var errorDescription: String?](managedappdistributionerror/errordescription.md)
  A brief description of the error.
- [var failureReason: String?](managedappdistributionerror/failurereason.md)
  A detailed description of the error.
- [var recoveryOptions: [String]](managedappdistributionerror/recoveryoptions.md)
  A set of possible recovery options to present.
- [var recoverySuggestion: String?](managedappdistributionerror/recoverysuggestion.md)
  A suggestion for recovering from the error.
- [var localizedStringResource: LocalizedStringResource](managedappdistributionerror/localizedstringresource.md)
  A set of localized error strings.
### Providing help information
- [var helpAnchor: String?](managedappdistributionerror/helpanchor.md)
  A link to help documentation.
### Recovering from errors
- [func attemptRecovery(optionIndex: Int) -> Bool](managedappdistributionerror/attemptrecovery(optionindex:).md)
  Attempt to recover from this error when someone selects the option at the given index.
- [func attemptRecovery(optionIndex: Int, resultHandler: (Bool) -> Void)](managedappdistributionerror/attemptrecovery(optionindex:resulthandler:).md)
  Attempt to recover from this error when someone selects the option at the given index.
### Operators
- [static func == (ManagedAppDistributionError, ManagedAppDistributionError) -> Bool](managedappdistributionerror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [ManagedAppDistributionError.appNotManaged](managedappdistributionerror/appnotmanaged.md)
  An error that indicates that the calling app is not managed
- [ManagedAppDistributionError.licenseNotFound](managedappdistributionerror/licensenotfound.md)
  An error that indicates that a license wasn’t found for requested app.
### Instance Properties
- [var hashValue: Int](managedappdistributionerror/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](managedappdistributionerror/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](managedappdistributionerror/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](managedappdistributionerror/equatable-implementations.md)
- [Error Implementations](managedappdistributionerror/error-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [RecoverableError](../Foundation/RecoverableError.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappdistributionerror)*