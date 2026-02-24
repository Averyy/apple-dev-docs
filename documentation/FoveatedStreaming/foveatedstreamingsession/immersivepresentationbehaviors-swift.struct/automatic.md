# automatic(_:_:)

**Framework**: Foveated Streaming  
**Kind**: method

Opens the immersive space when the session connects or resumes and dismisses the immersive space when the session pauses or disconnects.

**Availability**:
- visionOS 26.4+ (Beta)

## Declaration

```swift
static func automatic(_ open: OpenImmersiveSpaceAction, _ dismiss: DismissImmersiveSpaceAction) -> FoveatedStreamingSession.ImmersivePresentationBehaviors
```

## Parameters

- `open`: The action that opens the immersive space.
- `dismiss`: The action that dismisses the immersive space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/immersivepresentationbehaviors-swift.struct/automatic(_:_:))*