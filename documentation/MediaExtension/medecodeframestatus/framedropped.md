# frameDropped

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Type Property

A frame decode operation status that indicates the system dropped the output of the frame for a reason other than an error.

**Availability**:
- macOS 14.0+

## Declaration

```swift
static var frameDropped: MEDecodeFrameStatus { get }
```

```c
MEDecodeFrameFrameDropped
```

## Discussion

The decoder sets this value if [`doNotOutputFrame`](../medecodeframeoptions/donotoutputframe.md) is [`true`](../../Swift/true.md).

## See Also

### Inspecting a status
- [MEDecodeFrameNoStatus](./medecodeframenostatus.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/medecodeframestatus/framedropped)*