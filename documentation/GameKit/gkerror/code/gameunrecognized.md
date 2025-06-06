# GKError.Code.gameUnrecognized

**Framework**: GameKit  
**Kind**: case

The system can’t complete the requested operation because Game Center doesn’t recognize the app.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case gameUnrecognized
```

#### Discussion

Ensure the app’s `bundleID` is correct.

## See Also

- [GKError.Code.notSupported](gkerror/code/notsupported.md)
  The app doesn’t have Game Center enabled.
- [GKError.Code.appUnlisted](gkerror/code/appunlisted.md)
  The system can’t complete the requested operation because the game isn’t available on the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkerror/code/gameunrecognized)*