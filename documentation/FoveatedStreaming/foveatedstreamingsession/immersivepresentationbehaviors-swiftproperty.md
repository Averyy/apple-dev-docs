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

Use this property to control when the immersive space displaying the streamed content is presented and dismissed, or remove automatic presentation entirely. The default value is an empty array, indicating no automatic presentation behavior.

Some of the presentation behaviors you can use are as follows:

```swift
// Acquire open and dismiss actions from your SwiftUI environment.
@Environment(\.openImmersiveSpace) var open
@Environment(\.dismissImmersiveSpace) var dismiss

let session: FoveatedStreamingSession

// Present the immersive space when streaming begins (connect, resume),
// and dismiss the immersive space when streaming ends (disconnect, pause).
session.immersivePresentationBehaviors = .automatic(open, dismiss)

// Present the immersive space on connect, and dismiss the immersive space on disconnect.
// Do nothing on pause/resume.
session.immersivePresentationBehaviors = [.presentOnConnect(open), .dismissOnDisconnect(dismiss)]

// Disable all automatic presentation behaviors.
// You must manually call `open` and `dismiss` to control presentation.
session.immersivePresentationBehaviors = []
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/immersivepresentationbehaviors-swift.property)*