# SCClipBufferingOutputDelegate

**Framework**: ScreenCaptureKit  
**Kind**: protocol

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol SCClipBufferingOutputDelegate : NSObjectProtocol
```

#### Overview

Defines an interface for delegates of SCClipBufferingOutput to respond to events that occur during clip buffering.

## Topics

### Instance Methods
- [func clipBufferingOutput(SCClipBufferingOutput, didFailWithError: any Error)](scclipbufferingoutputdelegate/clipbufferingoutput(_:didfailwitherror:).md)
- [func clipBufferingOutputDidStartBuffering(SCClipBufferingOutput)](scclipbufferingoutputdelegate/clipbufferingoutputdidstartbuffering(_:).md)
- [func clipBufferingOutputDidStopBuffering(SCClipBufferingOutput)](scclipbufferingoutputdelegate/clipbufferingoutputdidstopbuffering(_:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scclipbufferingoutputdelegate)*