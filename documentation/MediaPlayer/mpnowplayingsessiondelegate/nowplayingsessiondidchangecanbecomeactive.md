# nowPlayingSessionDidChangeCanBecomeActive(_:)

**Framework**: Media Player  
**Kind**: method

Tells the delegate that the session is eligible to become active.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func nowPlayingSessionDidChangeCanBecomeActive(_ nowPlayingSession: MPNowPlayingSession)
```

## Parameters

- `nowPlayingSession`: The Now Playing session that changed.

## See Also

- [var canBecomeActive: Bool](mpnowplayingsession/canbecomeactive.md)
  A Boolean value that indicates whether the session can become the app’s active Now Playing session.
- [func nowPlayingSessionDidChangeActive(MPNowPlayingSession)](mpnowplayingsessiondelegate/nowplayingsessiondidchangeactive(_:).md)
  Tells the delegate that the session changed its active status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayingsessiondelegate/nowplayingsessiondidchangecanbecomeactive(_:))*