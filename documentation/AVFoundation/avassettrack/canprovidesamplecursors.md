# canProvideSampleCursors

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the track can provide instances of sample cursors to traverse its media samples and discover information.

**Availability**:
- macOS 10.10+ - Deprecated in 13.0

> **Deprecated**: Load the value of [`canProvideSampleCursors`](../avpartialasyncproperty/canprovidesamplecursors.md) asynchronously instead.

## Declaration

```swift
var canProvideSampleCursors: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL canProvideSampleCursors;
```

## See Also

### Creating sample cursors
- [- makeSampleCursorWithPresentationTimeStamp:](./makesamplecursor%28presentationtimestamp%29.md)
  Creates a sample cursor and positions it at or near the specified presentation timestamp.
- [- makeSampleCursorAtFirstSampleInDecodeOrder](./makesamplecursoratfirstsampleindecodeorder%28%29.md)
  Creates a sample cursor and positions it at the track’s first media sample in decode order.
- [- makeSampleCursorAtLastSampleInDecodeOrder](./makesamplecursoratlastsampleindecodeorder%28%29.md)
  Creates a sample cursor and positions it at the track’s last media sample in decode order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/canprovidesamplecursors)*