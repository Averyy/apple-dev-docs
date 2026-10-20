# delegate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A delegate object for the playback coordinator.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any AVPlayerPlaybackCoordinatorDelegate)? { get set }
```

```objc
@property (weak) id<AVPlayerPlaybackCoordinatorDelegate> delegate;
```

## See Also

### Configuring the delegate
- [protocol AVPlayerPlaybackCoordinatorDelegate](../avplayerplaybackcoordinatordelegate.md)
  A protocol that defines the methods to implement to participate in playback coordination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerplaybackcoordinator/delegate)*