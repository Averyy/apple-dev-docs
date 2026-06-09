# immersiveScene

**Framework**: Foveated Streaming  
**Kind**: property  
**Required**: Yes

The SwiftUI view that renders the streamed content.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
@ViewBuilder
@MainActor var immersiveScene: Self.Content { get }
```

#### Discussion

This view will be displayed in an immersive space by the extension. Typically this will be a `RealityView` that renders the 3D streamed content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingprovider/immersivescene)*