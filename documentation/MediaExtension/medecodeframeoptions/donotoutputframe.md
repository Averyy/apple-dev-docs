# doNotOutputFrame

**Framework**: MediaExtension  
**Kind**: property

A Boolean value that hints to the decoder whether or not it should emit an image buffer for the frame.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var doNotOutputFrame: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), the decoder emits [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) instead of a [`CVImageBuffer`](https://developer.apple.com/documentation/CoreVideo/cvimagebuffer-q40) instance.

## See Also

- [var realTimePlayback: Bool](medecodeframeoptions/realtimeplayback.md)
  A Boolean value that hints to the decoder to use a low-power mode that can’t decode faster than 1x real-time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/medecodeframeoptions/donotoutputframe)*