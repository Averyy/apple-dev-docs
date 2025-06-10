# isObservationEnabled

**Framework**: AVFoundation  
**Kind**: property

AVPlayer and other AVFoundation types can optionally be observed using Swift Observation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
class var isObservationEnabled: Bool { get set }
```

#### Discussion

When set to YES, new instances of AVPlayer, AVQueuePlayer, AVPlayerItem, and AVPlayerItemTrack are observable with Swift Observation. The default value is NO (not observable).  An exception is thrown if this property is set YES after initializing any objects of these types, or if it is set to NO after any observable objects are initialized.  In other words, all objects of these types must either be observable or not observable in an application instance.

For more information regarding management of class objects in SwiftUI, please refer to https://developer.apple.com/documentation/swiftui/state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/isobservationenabled)*