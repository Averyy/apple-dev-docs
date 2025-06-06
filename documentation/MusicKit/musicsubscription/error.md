# MusicSubscription.Error

**Framework**: MusicKit  
**Kind**: enum

An error that MusicKit can throw upon requesting the current music subscription of the user.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum Error
```

## Topics

### Enumeration Cases
- [MusicSubscription.Error.permissionDenied](musicsubscription/error/permissiondenied.md)
  An error indicating that the user doesn’t consent for your app to access their Apple Music data.
- [MusicSubscription.Error.privacyAcknowledgementRequired](musicsubscription/error/privacyacknowledgementrequired.md)
  An error indicating that the user needs to acknowledge the most-recent privacy policy for Apple Music.
- [MusicSubscription.Error.unknown](musicsubscription/error/unknown.md)
  An error indicating the ocurrence of an unknown or unexpected error.
### Initializers
- [init?(rawValue: String)](musicsubscription/error/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var errorDescription: String?](musicsubscription/error/errordescription.md)
  A localized message describing what error occurred.
- [var failureReason: String?](musicsubscription/error/failurereason.md)
  A localized message describing the reason for the failure.
- [var helpAnchor: String?](musicsubscription/error/helpanchor.md)
  A localized message providing “help” text if the user requests help.
- [var rawValue: String](musicsubscription/error/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [var recoverySuggestion: String?](musicsubscription/error/recoverysuggestion.md)
  A localized message describing how one might recover from the failure.
### Type Aliases
- [MusicSubscription.Error.RawValue](musicsubscription/error/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [CustomStringConvertible Implementations](musicsubscription/error/customstringconvertible-implementations.md)
- [Equatable Implementations](musicsubscription/error/equatable-implementations.md)
- [Error Implementations](musicsubscription/error/error-implementations.md)
- [RawRepresentable Implementations](musicsubscription/error/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicsubscription/error)*