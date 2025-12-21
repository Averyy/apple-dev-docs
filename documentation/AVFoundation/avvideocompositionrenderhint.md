# AVVideoCompositionRenderHint

**Framework**: AVFoundation  
**Kind**: class

Information about upcoming composition requests, such as composition start time and end time.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class AVVideoCompositionRenderHint
```

## Topics

### Managing composition timing
- [var startCompositionTime: CMTime](avvideocompositionrenderhint/startcompositiontime.md)
  The start time of the upcoming composition requests.
- [var endCompositionTime: CMTime](avvideocompositionrenderhint/endcompositiontime.md)
  The end time of the upcoming composition requests.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func anticipateRendering(using: AVVideoCompositionRenderHint)](avvideocompositing/anticipaterendering(using:).md)
  Informs a custom video compositor about upcoming rendering requests.
- [func prerollForRendering(using: AVVideoCompositionRenderHint)](avvideocompositing/prerollforrendering(using:).md)
  Tells a custom video compositor to perform any work in the prerolling phase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionrenderhint)*