# pushStreamNodes

**Framework**: PHASE  
**Kind**: property

A collection of audio streams for playback.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var pushStreamNodes: [String : PHASEPushStreamNode] { get }
```

#### Discussion

This dictionary populates a push-stream node for sound events that PHASE generates for [`PHASEPushStreamNodeDefinition`](phasepushstreamnodedefinition.md) in your event node tree. The dictionary key is the stream-node definition’s [`identifier`](phasedefinition/identifier.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/pushstreamnodes)*