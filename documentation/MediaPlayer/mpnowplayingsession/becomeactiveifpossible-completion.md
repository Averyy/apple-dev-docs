# becomeActiveIfPossible(completion:)

**Framework**: Media Player  
**Kind**: method

Tells the system to make the session the active Now Playing session if possible.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func becomeActiveIfPossible() async -> Bool
```

## Parameters

- `completion`: The completion handler the system calls after it processes the request.

## See Also

- [var isActive: Bool](mpnowplayingsession/isactive.md)
  A Boolean value that indicates whether the session is the app’s active Now Playing session.
- [var canBecomeActive: Bool](mpnowplayingsession/canbecomeactive.md)
  A Boolean value that indicates whether the session can become the app’s active Now Playing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayingsession/becomeactiveifpossible(completion:))*