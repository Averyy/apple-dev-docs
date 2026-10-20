# makeSampleCursor(presentationTimeStamp:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Creates a sample cursor and positions it at or near the specified presentation timestamp.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 10.10+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func makeSampleCursor(presentationTimeStamp: CMTime) -> AVSampleCursor?
```

```objc
- (AVSampleCursor *) makeSampleCursorWithPresentationTimeStamp:(CMTime) presentationTimeStamp;
```

#### Return Value

An instance of [`AVSampleCursor`](../avsamplecursor.md).

#### Discussion

If the track’s [`asset`](./asset.md) property value for [`providesPreciseDurationAndTiming`](../avasset/providesprecisedurationandtiming.md) is [`true`](../../Swift/true.md), the sample cursor is accurately positioned at the track’slast media sample with a presentation timestamp less than or equal to the desired timestamp, or, if there are no such samples, the first sample in presentation order.

If the track’s [`asset`](./asset.md) property value for [`providesPreciseDurationAndTiming`](../avasset/providesprecisedurationandtiming.md) is [`false`](../../Swift/false.md), and it’s prohibitively expensive to locate the precise sample at the desired timestamp, the sample cursor may be approximately positioned.

## Parameters

- `presentationTimeStamp`: The initial presentation timestamp of the sample cursor.

## See Also

### Creating sample cursors
- [func makeSampleCursorAtFirstSampleInDecodeOrder() -> AVSampleCursor?](./makesamplecursoratfirstsampleindecodeorder%28%29.md)
  Creates a sample cursor and positions it at the track’s first media sample in decode order.
- [func makeSampleCursorAtLastSampleInDecodeOrder() -> AVSampleCursor?](./makesamplecursoratlastsampleindecodeorder%28%29.md)
  Creates a sample cursor and positions it at the track’s last media sample in decode order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/makesamplecursor(presentationtimestamp:))*