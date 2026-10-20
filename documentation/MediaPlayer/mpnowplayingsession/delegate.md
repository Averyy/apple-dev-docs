# delegate

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The Now Playing session’s delegate object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any MPNowPlayingSessionDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<MPNowPlayingSessionDelegate> delegate;
```

## See Also

### Accessing the delegate object
- [protocol MPNowPlayingSessionDelegate](../mpnowplayingsessiondelegate.md)
  A protocol that defines the delegate interface for a Now Playing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpnowplayingsession/delegate)*