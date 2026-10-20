# nextCaptionGroup()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns the next caption group.

**Availability**:
- iOS 18.0+ - Deprecated in 27.0
- iPadOS 18.0+ - Deprecated in 27.0
- Mac Catalyst 15.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAssetReader.outputCaptionProvider(for:validationDelegate:) instead

## Declaration

```swift
func nextCaptionGroup() -> AVCaptionGroup?
```

```objc
- (AVCaptionGroup *) nextCaptionGroup;
```

#### Return Value

The caption group, or `nil` of there are no more groups.

## See Also

### Reading caption groups
- [func captionsNotPresentInPreviousGroups(in: AVCaptionGroup) -> [AVCaption]](./captionsnotpresentinpreviousgroups%28in%29.md)
  Returns the set of captions in the caption group that weren’t vended by the adaptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutputcaptionadaptor/nextcaptiongroup())*