# SCClipBufferingOutputDelegate

**Framework**: ScreenCaptureKit  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol SCClipBufferingOutputDelegate <NSObject>
```

## Overview

Defines an interface for delegates of SCClipBufferingOutput to respond to events that occur during clip buffering.

## Topics

### Instance Methods
- [func clipBufferingOutput(SCClipBufferingOutput, didFailWithError: any Error)](./scclipbufferingoutputdelegate/clipbufferingoutput%28_,didfailwitherror%29.md)
- [func clipBufferingOutputDidStartBuffering(SCClipBufferingOutput)](./scclipbufferingoutputdelegate/clipbufferingoutputdidstartbuffering%28_%29.md)
- [func clipBufferingOutputDidStopBuffering(SCClipBufferingOutput)](./scclipbufferingoutputdelegate/clipbufferingoutputdidstopbuffering%28_%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scclipbufferingoutputdelegate)*