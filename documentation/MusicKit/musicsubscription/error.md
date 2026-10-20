# MusicSubscription.Error

**Framework**: MusicKit  
**Kind**: enum  
**Role**: Enumeration

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
- [MusicSubscription.Error.permissionDenied](./error/permissiondenied.md)
  An error indicating that the user doesn’t consent for your app to access their Apple Music data.
- [MusicSubscription.Error.privacyAcknowledgementRequired](./error/privacyacknowledgementrequired.md)
  An error indicating that the user needs to acknowledge the most-recent privacy policy for Apple Music.
- [MusicSubscription.Error.unknown](./error/unknown.md)
  An error indicating the ocurrence of an unknown or unexpected error.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicsubscription/error)*