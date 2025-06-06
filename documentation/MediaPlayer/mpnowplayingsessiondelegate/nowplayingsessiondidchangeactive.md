# nowPlayingSessionDidChangeActive(_:)

**Framework**: Media Player  
**Kind**: method

Tells the delegate that the session changed its active status.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func nowPlayingSessionDidChangeActive(_ nowPlayingSession: MPNowPlayingSession)
```

## Parameters

- `nowPlayingSession`: The Now Playing session that changed.

## See Also

- [var isActive: Bool](mpnowplayingsession/isactive.md)
  A Boolean value that indicates whether the session is the app’s active Now Playing session.
- [func nowPlayingSessionDidChangeCanBecomeActive(MPNowPlayingSession)](mpnowplayingsessiondelegate/nowplayingsessiondidchangecanbecomeactive(_:).md)
  Tells the delegate that the session is eligible to become active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayingsessiondelegate/nowplayingsessiondidchangeactive(_:))*