# frameDropped

**Framework**: MediaExtension  
**Kind**: property

A frame decode operation status that indicates the system dropped the output of the frame for a reason other than an error.

**Availability**:
- macOS 14.0+

## Declaration

```swift
static var frameDropped: MEDecodeFrameStatus { get }
```

#### Discussion

The decoder sets this value if [`doNotOutputFrame`](medecodeframeoptions/donotoutputframe.md) is [`true`](https://developer.apple.com/documentation/Swift/true).


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/medecodeframestatus/framedropped)*