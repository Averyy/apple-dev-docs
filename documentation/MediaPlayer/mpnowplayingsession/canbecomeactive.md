# canBecomeActive

**Framework**: Media Player  
**Kind**: property

A Boolean value that indicates whether the session can become the app’s active Now Playing session.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var canBecomeActive: Bool { get }
```

## See Also

- [var isActive: Bool](mpnowplayingsession/isactive.md)
  A Boolean value that indicates whether the session is the app’s active Now Playing session.
- [func becomeActiveIfPossible(completion: ((Bool) -> Void)?)](mpnowplayingsession/becomeactiveifpossible(completion:).md)
  Tells the system to make the session the active Now Playing session if possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayingsession/canbecomeactive)*