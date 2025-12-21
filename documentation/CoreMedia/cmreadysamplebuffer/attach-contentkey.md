# attach(contentKey:)

**Framework**: Core Media  
**Kind**: method

Attaches an AVContentKey to a CMReadySampleBuffer for the purpose of content decryption. The client is expected to attach AVContentKeys to CMReadySampleBuffers that have been created by the client for enqueueing with AVSampleBufferDisplayLayer or AVSampleBufferAudioRenderer, for which the AVContentKeySpecifier matches indications of suitability that are available to the client according to the content key system that’s in use.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
mutating func attach(contentKey: AVContentKey) throws
```

#### Discussion

> **Note**: Describes the reason for failure to attach the content key.

## Parameters

- `contentKey`: The content key to be attached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadysamplebuffer/attach(contentkey:))*