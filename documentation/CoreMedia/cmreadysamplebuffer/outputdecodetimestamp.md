# outputDecodeTimeStamp

**Framework**: Core Media  
**Kind**: property  
**Role**: Instance Property

The output decode timestamp of the sample buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var outputDecodeTimeStamp: CMTime { get }
```

#### Discussion

For consistency with [`outputPresentationTimeStamp`](./outputpresentationtimestamp.md), this is calculated as: `OutputPresentationTimeStamp + ((DecodeTimeStamp - PresentationTimeStamp) / SpeedMultiplier)`.

- OutputPresentationTimeStamp is [`outputPresentationTimeStamp`](./outputpresentationtimestamp.md) property of this sample buffer.
- PresentationTimeStamp is `presentationTimeStamp` property of this sample buffer.
- DecodeTimeStamp is [`decodeTimeStamp`](./decodetimestamp.md) property of this sample buffer.
- SpeedMultiplier is the value of [`speedMultiplier`](../cmsamplebuffer/attachmentkey/speedmultiplier.md) attachment (default 1).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadysamplebuffer/outputdecodetimestamp)*