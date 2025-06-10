# captionsNotPresentInPreviousGroups(in:)

**Framework**: AVFoundation  
**Kind**: method

Returns the set of captions that are present in the given group but were not present in any group previously vended by calls to next().

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
func captionsNotPresentInPreviousGroups(in captionGroup: AVCaptionGroup) -> [AVCaption]
```

#### Return Value

An array of AVCaption objects.

## Parameters

- `captionGroup`: The group containing the captions of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/provider/captionsnotpresentinpreviousgroups(in:))*