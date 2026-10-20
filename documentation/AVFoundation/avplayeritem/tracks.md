# tracks

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of player item track objects.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
nonisolated
var tracks: [AVPlayerItemTrack] { get }
```

```objc
@property (readonly) NSArray<AVPlayerItemTrack *> * tracks;
```

#### Discussion

The value is an empty array before the player loads the underlying tracks. Key-value observe this property value to access valid tracks as soon as they’re available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/tracks)*