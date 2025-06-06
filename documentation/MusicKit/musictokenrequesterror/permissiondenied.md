# MusicTokenRequestError.permissionDenied

**Framework**: MusicKit  
**Kind**: case

An error that occurs when the user doesn’t consent for the current app to access their Apple Music data.

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
case permissionDenied
```

#### Discussion

Apps using MusicKit need to request prior informed consent from the user to access their Apple Music data by calling [`request()`](musicauthorization/request().md) at the appropriate point in the app flow, right before needing to use other APIs from MusicKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musictokenrequesterror/permissiondenied)*