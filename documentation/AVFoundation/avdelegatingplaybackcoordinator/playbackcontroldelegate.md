# playbackControlDelegate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The delegate object for the playback coordinator.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
weak var playbackControlDelegate: (any AVPlaybackCoordinatorPlaybackControlDelegate)? { get }
```

```objc
@property (nonatomic, weak, readonly) id<AVPlaybackCoordinatorPlaybackControlDelegate> playbackControlDelegate;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinator/playbackcontroldelegate)*