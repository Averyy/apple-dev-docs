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
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicsubscription/error)*