# FoveatedStreamingSession.ImmersivePresentationBehaviors

**Framework**: Foveated Streaming  
**Kind**: struct

The presentation behaviors describing when the immersive space that hosts the streamed content is presented and dismissed.

**Availability**:
- visionOS 26.4+ (Beta)

## Declaration

```swift
struct ImmersivePresentationBehaviors
```

#### Overview

Use `ImmersivePresentationBehaviors` to automatically present the immersive space when the foveated streaming session connects or resumes, as well as automatically dismiss the immersive space when the foveated streaming session pauses or disconnects.

## Topics

### Initializers
- [init()](foveatedstreamingsession/immersivepresentationbehaviors-swift.struct/init.md)
### Type Methods
- [static func automatic(OpenImmersiveSpaceAction, DismissImmersiveSpaceAction) -> FoveatedStreamingSession.ImmersivePresentationBehaviors](foveatedstreamingsession/immersivepresentationbehaviors-swift.struct/automatic(_:_:).md)
  Opens the immersive space when the session connects or resumes and dismisses the immersive space when the session pauses or disconnects.
- [static func dismissOnDisconnect(DismissImmersiveSpaceAction) -> FoveatedStreamingSession.ImmersivePresentationBehaviors](foveatedstreamingsession/immersivepresentationbehaviors-swift.struct/dismissondisconnect(_:).md)
  Dismisses the immersive space when the session disconnects.
- [static func dismissOnPause(DismissImmersiveSpaceAction) -> FoveatedStreamingSession.ImmersivePresentationBehaviors](foveatedstreamingsession/immersivepresentationbehaviors-swift.struct/dismissonpause(_:).md)
  Dismisses the immersive space when the session pauses.
- [static func presentOnConnect(OpenImmersiveSpaceAction) -> FoveatedStreamingSession.ImmersivePresentationBehaviors](foveatedstreamingsession/immersivepresentationbehaviors-swift.struct/presentonconnect(_:).md)
  Opens the immersive space when the session connects.
- [static func presentOnResume(OpenImmersiveSpaceAction) -> FoveatedStreamingSession.ImmersivePresentationBehaviors](foveatedstreamingsession/immersivepresentationbehaviors-swift.struct/presentonresume(_:).md)
  Opens the immersive space when the session resumes.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Escapable](../Swift/Escapable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/immersivepresentationbehaviors-swift.struct)*