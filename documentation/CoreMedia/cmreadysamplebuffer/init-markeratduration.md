# init(markerAt:duration:)

**Framework**: Core Media  
**Kind**: init

Creates a marker-only sample buffer with no payload and no format description.

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
init(markerAt markerTime: CMTime, duration: CMTime = .invalid)
```

#### Discussion

Marker-only sample buffers are meant to carry attachments that communicate a state change between sample buffers. To set attachments on the sample buffer please to access the underlying sample buffer instance as follows:

```swift
markerOnlySampleBuffer.withUnsafeSampleBuffer { sbuf in
    sbuf.attachments[.endsPreviousSampleDuration] = .shouldPropagate(true)
}
```

## Parameters

- `markerTime`: Timestamp at which the marker sample buffer should be considered. Pass    if the marker buffer does not carry timing information.
- `duration`: Duration of the marker sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadysamplebuffer/init(markerat:duration:))*