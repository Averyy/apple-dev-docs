# makeSampleCursorAtFirstSampleInDecodeOrder()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Creates a sample cursor and positions it at the track’s first media sample in decode order.

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
func makeSampleCursorAtFirstSampleInDecodeOrder() -> AVSampleCursor?
```

```objc
- (AVSampleCursor *) makeSampleCursorAtFirstSampleInDecodeOrder;
```

#### Return Value

An instance of [`AVSampleCursor`](../avsamplecursor.md).

## See Also

### Creating sample cursors
- [func makeSampleCursor(presentationTimeStamp: CMTime) -> AVSampleCursor?](./makesamplecursor%28presentationtimestamp%29.md)
  Creates a sample cursor and positions it at or near the specified presentation timestamp.
- [func makeSampleCursorAtLastSampleInDecodeOrder() -> AVSampleCursor?](./makesamplecursoratlastsampleindecodeorder%28%29.md)
  Creates a sample cursor and positions it at the track’s last media sample in decode order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/makesamplecursoratfirstsampleindecodeorder())*