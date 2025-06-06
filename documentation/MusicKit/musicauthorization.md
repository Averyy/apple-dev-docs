# MusicAuthorization

**Framework**: MusicKit  
**Kind**: struct

A type that allows you to request the user’s informed consent for your app to access their music data.

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
struct MusicAuthorization
```

## Topics

### Type Properties
- [static var currentStatus: MusicAuthorization.Status](musicauthorization/currentstatus.md)
  The authorization status the user sets for accessing MusicKit.
### Type Methods
- [static func request() async -> MusicAuthorization.Status](musicauthorization/request.md)
  Asks the user for permission for the current app to access MusicKit.
### Enumerations
- [MusicAuthorization.Status](musicauthorization/status.md)
  A value that indicates the authorization status the user sets for the current app to access their Apple Music data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicauthorization)*