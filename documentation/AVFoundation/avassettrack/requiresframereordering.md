# requiresFrameReordering

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether samples in the track may have different presentation and decode timestamps.

**Availability**:
- iOS 8.0+ - Deprecated in 16.0
- iPadOS 8.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.10+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- watchOS 1.0+ - Deprecated in 9.0

> **Deprecated**: Load the value of [`requiresFrameReordering`](../avpartialasyncproperty/requiresframereordering.md) asynchronously instead.

## Declaration

```swift
var requiresFrameReordering: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL requiresFrameReordering;
```

## See Also

### Accessing frame-based characteristics
- [nominalFrameRate](./nominalframerate.md)
  The frame rate of the track, in frames per second.
- [minFrameDuration](./minframeduration.md)
  The minimum duration of the track’s frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/requiresframereordering)*