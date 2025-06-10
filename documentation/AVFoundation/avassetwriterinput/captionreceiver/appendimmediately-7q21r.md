# appendImmediately(_:)

**Framework**: AVFoundation  
**Kind**: method

Appends the caption group synchronously if the input is ready for more media data.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
func appendImmediately(_ captionGroup: AVCaptionGroup) throws -> Bool
```

#### Return Value

Returns true if the append was successful, false if the input was not ready for more media data.

#### Discussion

> **Note**: An error if the underlying writer failed.

## Parameters

- `captionGroup`: The caption group to be appended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/captionreceiver/appendimmediately(_:)-7q21r)*