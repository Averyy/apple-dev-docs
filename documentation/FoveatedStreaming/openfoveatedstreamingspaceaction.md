# OpenFoveatedStreamingSpaceAction

**Framework**: Foveated Streaming  
**Kind**: struct

An action that presents a foveated streaming space.

**Availability**:
- visionOS 26.4+ (Beta)

## Declaration

```swift
@MainActor
struct OpenFoveatedStreamingSpaceAction
```

#### Overview

Use the [`openFoveatedStreamingSpace`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/openFoveatedStreamingSpace) environment value to get the instance of this structure for a given [`Environment`](https://developer.apple.com/documentation/SwiftUI/Environment). Then call the instance to present a space. You call the instance directly because it defines [`callAsFunction(for:)`](openfoveatedstreamingspaceaction/callasfunction(for:).md) methods that Swift calls when you call the instance.

## Topics

### Instance Methods
- [func callAsFunction(for: FoveatedStreamingSession) async -> OpenImmersiveSpaceAction.Result](openfoveatedstreamingspaceaction/callasfunction(for:).md)
  Presents the foveated streaming space that your app defines for the specified foveated streaming session.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class FoveatedStreamingSession](foveatedstreamingsession.md)
  A session that manages a foveated streaming connection to a local or remote streaming endpoint.
- [struct FoveatedStreamingSpace](foveatedstreamingspace.md)
  An immersive space that displays foveated streaming content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/openfoveatedstreamingspaceaction)*