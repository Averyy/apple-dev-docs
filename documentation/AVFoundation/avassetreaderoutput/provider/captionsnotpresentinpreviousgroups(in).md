# captionsNotPresentInPreviousGroups(in:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns the set of captions that are present in the given group but were not present in any group previously vended by calls to next().

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
func captionsNotPresentInPreviousGroups(in captionGroup: AVCaptionGroup) -> [AVCaption]
```

Available when `Payload` is `AVCaptionGroup`.

## Return Value

An array of AVCaption objects.

## Parameters

- `captionGroup`: The group containing the captions of interest.

## See Also

### Reading media data
- [func next() async throws -> Payload?](./next%28%29.md)
  Returns the next piece of media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput/provider/captionsnotpresentinpreviousgroups(in:))*