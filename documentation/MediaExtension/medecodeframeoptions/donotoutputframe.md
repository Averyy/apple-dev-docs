# doNotOutputFrame

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

A Boolean value that hints to the decoder whether or not it should emit an image buffer for the frame.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var doNotOutputFrame: Bool { get set }
```

```objc
@property (readwrite) BOOL doNotOutputFrame;
```

#### Discussion

If [`true`](../../Swift/true.md), the decoder emits [`nil`](../../ObjectiveC/nil-227m0.md) instead of a [CVImageBuffer](../../CoreVideo/cvimagebuffer-q40.md) instance.

## See Also

### Inspecting frame decoding options
- [var realTimePlayback: Bool](./realtimeplayback.md)
  A Boolean value that hints to the decoder to use a low-power mode that can’t decode faster than 1x real-time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/medecodeframeoptions/donotoutputframe)*