# clipBufferingOutput(_:didFailWithError:)

**Framework**: ScreenCaptureKit  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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