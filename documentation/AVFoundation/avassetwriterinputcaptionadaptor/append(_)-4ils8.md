# append(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Appends a caption group that the system writes to the output.

**Availability**:
- iOS 18.0+ - Deprecated in 27.0
- iPadOS 18.0+ - Deprecated in 27.0
- Mac Catalyst 15.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAssetWriter.inputCaptionReceiver(for:) instead

## Declaration

```swift
func append(_ captionGroup: AVCaptionGroup) -> Bool
```

```objc
- (BOOL) appendCaptionGroup:(AVCaptionGroup *) captionGroup;
```

## Return Value

A Boolean value that indicates whether the operation succeeded.

## Parameters

- `captionGroup`: The caption group that the system writes to the output.

## See Also

### Appending captions
- [func append(AVCaption) -> Bool](./append%28_%29-910lp.md)
  Appends a caption to the writer input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputcaptionadaptor/append(_:)-4ils8)*