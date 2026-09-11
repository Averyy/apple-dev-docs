# transitionID

**Framework**: Core Media  
**Kind**: property

Marks a transition from one source of buffers to another.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static let transitionID: CVAttachmentKeyDefinition<CMSampleBufferAttachmentKeyDefinitions.ShouldNotPropagate, Int>
```

#### Discussion

During gapless playback of a list of songs, this attachment marks the first buffer from the next song. If this attachment is on a buffer containing no samples, the first following buffer that contains samples is the buffer that contains the first samples from the next song. This transition identifier should be unique within a playlist, so each transition in a playlist is uniquely identifiable. A counter that increments with each transition is a simple example.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferattachmentkeydefinitions/transitionid)*