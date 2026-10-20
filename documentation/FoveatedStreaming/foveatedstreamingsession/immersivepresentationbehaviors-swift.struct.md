# FoveatedStreamingSession.ImmersivePresentationBehaviors

**Framework**: Foveated Streaming  
**Kind**: struct  
**Role**: Structure

The presentation behaviors describing when the immersive space that hosts the streamed content is presented and dismissed.

**Availability**:
- visionOS 26.4+

## Declaration

```swift
struct ImmersivePresentationBehaviors
```

#### Overview

Use `ImmersivePresentationBehaviors` to automatically present the immersive space when the foveated streaming session connects or resumes, as well as automatically dismiss the immersive space when the foveated streaming session pauses or disconnects.

## Topics

### Initializers
- [init()](./immersivepresentationbehaviors-swift.struct/init%28%29.md)
### Type Methods
- [static func automatic(OpenImmersiveSpaceAction, DismissImmersiveSpaceAction) -> FoveatedStreamingSession.ImmersivePresentationBehaviors](./immersivepresentationbehaviors-swift.struct/automatic%28_,_%29.md)
  Opens the immersive space when the session connects or resumes and dismisses the immersive space when the session pauses or disconnects.
- [static func dismissOnDisconnect(DismissImmersiveSpaceAction) -> FoveatedStreamingSession.ImmersivePresentationBehaviors](./immersivepresentationbehaviors-swift.struct/dismissondisconnect%28_%29.md)
  Dismisses the immersive space when the session disconnects.
- [static func dismissOnPause(DismissImmersiveSpaceAction) -> FoveatedStreamingSession.ImmersivePresentationBehaviors](./immersivepresentationbehaviors-swift.struct/dismissonpause%28_%29.md)
  Dismisses the immersive space when the session pauses.
- [static func presentOnConnect(OpenImmersiveSpaceAction) -> FoveatedStreamingSession.ImmersivePresentationBehaviors](./immersivepresentationbehaviors-swift.struct/presentonconnect%28_%29.md)
  Opens the immersive space when the session connects.
- [static func presentOnResume(OpenImmersiveSpaceAction) -> FoveatedStreamingSession.ImmersivePresentationBehaviors](./immersivepresentationbehaviors-swift.struct/presentonresume%28_%29.md)
  Opens the immersive space when the session resumes.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/immersivepresentationbehaviors-swift.struct)*