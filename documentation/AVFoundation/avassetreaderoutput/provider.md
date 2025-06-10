# AVAssetReaderOutput.Provider

**Framework**: AVFoundation  
**Kind**: class

Defines an interface for reading a single collection of smaples of a common media type from an AVAssetReader.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class Provider<Payload> where Payload : AVAssetReaderOutput.SupportedPayload
```

## Topics

### Instance Methods
- [func captionsNotPresentInPreviousGroups(in: AVCaptionGroup) -> [AVCaption]](avassetreaderoutput/provider/captionsnotpresentinpreviousgroups(in:).md)
  Returns the set of captions that are present in the given group but were not present in any group previously vended by calls to next().
- [func next(isolation: isolated (any Actor)?) async throws -> Payload?](avassetreaderoutput/provider/next(isolation:).md)
  Retruns the next piece of media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/provider)*