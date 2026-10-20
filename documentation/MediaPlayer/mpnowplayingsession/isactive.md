# isActive

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the session is the app’s active Now Playing session.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var isActive: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isActive) BOOL active;
```

## See Also

### Managing the active state
- [var canBecomeActive: Bool](./canbecomeactive.md)
  A Boolean value that indicates whether the session can become the app’s active Now Playing session.
- [func becomeActiveIfPossible(completion: ((Bool) -> Void)?)](./becomeactiveifpossible%28completion%29.md)
  Tells the system to make the session the active Now Playing session if possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayingsession/isactive)*