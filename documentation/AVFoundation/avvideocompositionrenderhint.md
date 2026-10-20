# AVVideoCompositionRenderHint

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVVideoCompositionRenderHint : NSObject
```

## Topics

### Managing composition timing
- [var startCompositionTime: CMTime](./avvideocompositionrenderhint/startcompositiontime.md)
  The start time of the upcoming composition requests.
- [var endCompositionTime: CMTime](./avvideocompositionrenderhint/endcompositiontime.md)
  The end time of the upcoming composition requests.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Preparing to render frames
- [func anticipateRendering(using: AVVideoCompositionRenderHint)](./avvideocompositing/anticipaterendering%28using%29.md)
  Informs a custom video compositor about upcoming rendering requests.
- [func prerollForRendering(using: AVVideoCompositionRenderHint)](./avvideocompositing/prerollforrendering%28using%29.md)
  Tells a custom video compositor to perform any work in the prerolling phase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositionrenderhint)*