# immersivePresentationBehaviors

**Framework**: Foveated Streaming  
**Kind**: property

An optional set of behaviors which assist in automatically presenting the session’s immersive space.

**Availability**:
- visionOS 26.4+ (Beta)

## Declaration

```swift
@MainActor
final var immersivePresentationBehaviors: FoveatedStreamingSession.ImmersivePresentationBehaviors { get set }
```

#### Discussion

For example, you can use this to automatically present the FoveatedStreamingSpace on connect, or automatically dismiss the FoveatedStreamingSpace on disconnect.

```swift
// Acquire these actions from your SwiftUI environment.
@Environment(\.openFoveatedStreamingSpace) var open
@Environment(\.dismissImmersiveSpace) var dismiss

let session: FoveatedStreamingSession

// Present the immersive space when streaming begins (connect, resume),
// and dismiss the immersive space when streaming ends (disconnect, pause).
session.immersivePresentationBehaviors = .automatic(open, dismiss)

// Present the immersive space on connect, and dismiss the immersive space on disconnect.
// Do nothing on pause/resume.
session.immersivePresentationBehaviors = [.presentOnConnect(open), .dismissOnDisconnect(dismiss)]

// Disable all automatic presentation behaviors.
// You must manually call `openFoveatedStreamingSpace` and `dismissImmersiveSpace` to control presentation.
session.immersivePresentationBehaviors = []
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/immersivepresentationbehaviors-swift.property)*