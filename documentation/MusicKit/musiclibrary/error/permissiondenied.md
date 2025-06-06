# MusicLibrary.Error.permissionDenied

**Framework**: MusicKit  
**Kind**: case

An error that occurs when the user doesn’t consent for the current app to access their Apple Music library.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 16.1+
- visionOS 1.0+
- watchOS 9.1+

## Declaration

```swift
case permissionDenied
```

#### Discussion

Apps using MusicKit need to request prior informed consent from the user to access their Apple Music library by calling [`request()`](musicauthorization/request().md) at the appropriate point in the app flow, right before needing to use other APIs from MusicKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiclibrary/error/permissiondenied)*