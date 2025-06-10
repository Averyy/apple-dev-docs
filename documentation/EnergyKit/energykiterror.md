# EnergyKitError

**Framework**: EnergyKit  
**Kind**: enum

A specialized error that provides localized messages describing the error and why it occurred.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
enum EnergyKitError
```

## Topics

### Viewing error reasons
- [EnergyKitError.guidanceUnavailable](energykiterror/guidanceunavailable.md)
  The system failed to retrieve guidance for the requested location.
- [EnergyKitError.inProgress](energykiterror/inprogress.md)
  A request is already in progress.
- [EnergyKitError.invalidLoadEvent](energykiterror/invalidloadevent.md)
  The load event payload is invalid.
- [EnergyKitError.permissionDenied](energykiterror/permissiondenied.md)
  The client doesn’t have permission to access the requested API.
- [EnergyKitError.serviceUnavailable](energykiterror/serviceunavailable.md)
  The requested service failed to start.
- [EnergyKitError.venueUnavailable](energykiterror/venueunavailable.md)
  The requested energy venue doesn’t exist.
### Reading error messages
- [var errorDescription: String?](energykiterror/errordescription.md)
  A localized message describing what error occurred.
- [var failureReason: String?](energykiterror/failurereason.md)
  A localized message providing text if the person requests help.
- [var helpAnchor: String?](energykiterror/helpanchor.md)
  A localized message providing text if the user requests help
- [var recoverySuggestion: String?](energykiterror/recoverysuggestion.md)
  A localized message describing how to recover from the failure.
### Operators
- [static func == (EnergyKitError, EnergyKitError) -> Bool](energykiterror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](energykiterror/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](energykiterror/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](energykiterror/equatable-implementations.md)
- [Error Implementations](energykiterror/error-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/energykiterror)*