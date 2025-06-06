# captionsNotPresentInPreviousGroups(in:)

**Framework**: AVFoundation  
**Kind**: method

Returns the set of captions in the caption group that weren’t vended by the adaptor.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
func captionsNotPresentInPreviousGroups(in captionGroup: AVCaptionGroup) -> [AVCaption]
```

#### Return Value

An array of captions not previously vended by the adaptor, or an empty array if there are none.

## Parameters

- `captionGroup`: The caption group to query.

## See Also

- [func nextCaptionGroup() -> AVCaptionGroup?](avassetreaderoutputcaptionadaptor/nextcaptiongroup.md)
  Returns the next caption group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutputcaptionadaptor/captionsnotpresentinpreviousgroups(in:))*