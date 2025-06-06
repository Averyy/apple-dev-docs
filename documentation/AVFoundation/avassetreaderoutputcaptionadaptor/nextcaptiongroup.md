# nextCaptionGroup()

**Framework**: AVFoundation  
**Kind**: method

Returns the next caption group.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
func nextCaptionGroup() -> AVCaptionGroup?
```

#### Return Value

The caption group, or `nil` of there are no more groups.

## See Also

- [func captionsNotPresentInPreviousGroups(in: AVCaptionGroup) -> [AVCaption]](avassetreaderoutputcaptionadaptor/captionsnotpresentinpreviousgroups(in:).md)
  Returns the set of captions in the caption group that weren’t vended by the adaptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutputcaptionadaptor/nextcaptiongroup())*