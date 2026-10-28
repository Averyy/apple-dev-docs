# append(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Appends a caption to the writer input.

**Availability**:
- iOS 18.0+ - Deprecated in 27.0
- iPadOS 18.0+ - Deprecated in 27.0
- Mac Catalyst 15.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAssetWriter.inputCaptionReceiver(for:) instead

## Declaration

```swift
func append(_ caption: AVCaption) -> Bool
```

```objc
- (BOOL) appendCaption:(AVCaption *) caption;
```

## Return Value

A Boolean value that indicates whether the operation succeeded.

## Parameters

- `caption`: The caption that the system appends to the writer input.

## See Also

### Appending captions
- [func append(AVCaptionGroup) -> Bool](./append%28_%29-4ils8.md)
  Appends a caption group that the system writes to the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputcaptionadaptor/append(_:)-910lp)*