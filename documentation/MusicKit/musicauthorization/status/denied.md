# MusicAuthorization.Status.denied

**Framework**: MusicKit  
**Kind**: case

The user denied permission for the current app to use MusicKit.

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
case denied
```

#### Discussion

On iOS, applications may attempt to recover from this situation by suggesting to their users that they can grant access to their Apple Music data again by linking to [`openSettingsURLString`](https://developer.apple.com/documentation/UIKit/UIApplication/openSettingsURLString).


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicauthorization/status/denied)*