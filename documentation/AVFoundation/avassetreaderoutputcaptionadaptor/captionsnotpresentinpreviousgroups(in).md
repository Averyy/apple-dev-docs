# captionsNotPresentInPreviousGroups(in:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns the set of captions in the caption group that weren’t vended by the adaptor.

**Availability**:
- iOS 18.0+ - Deprecated in 27.0
- iPadOS 18.0+ - Deprecated in 27.0
- Mac Catalyst 15.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAssetReader.outputCaptionProvider(for:validationDelegate:) instead

## Declaration

```swift
func captionsNotPresentInPreviousGroups(in captionGroup: AVCaptionGroup) -> [AVCaption]
```

```objc
- (NSArray<AVCaption *> *) captionsNotPresentInPreviousGroupsInCaptionGroup:(AVCaptionGroup *) captionGroup;
```

#### Return Value

An array of captions not previously vended by the adaptor, or an empty array if there are none.

## Parameters

- `captionGroup`: The caption group to query.

## See Also

### Reading caption groups
- [func nextCaptionGroup() -> AVCaptionGroup?](./nextcaptiongroup%28%29.md)
  Returns the next caption group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutputcaptionadaptor/captionsnotpresentinpreviousgroups(in:))*