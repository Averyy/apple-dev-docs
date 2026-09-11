# clipBufferingOutput(_:didFailWithError:)

**Framework**: ScreenCaptureKit  
**Kind**: method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
optional func clipBufferingOutput(_ clipBufferingOutput: SCClipBufferingOutput, didFailWithError error: any Error)
```

#### Discussion

clipBufferingOutput:didFailWithError:

Notifies the delegate that clip buffering has failed with an associated error.

## Parameters

- `clipBufferingOutput`: The SCClipBufferingOutput object
- `error`: Error describing why clip buffering failed


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scclipbufferingoutputdelegate/clipbufferingoutput(_:didfailwitherror:))*