# appendImmediately(_:)

**Framework**: AVFoundation  
**Kind**: method

Appends the caption synchronously if the input is ready for more media data.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
func appendImmediately(_ caption: AVCaption) throws -> Bool
```

#### Return Value

Returns true if the append was successful, false if the input was not ready for more media data.

#### Discussion

> **Note**: An error if the underlying writer failed.

## Parameters

- `caption`: The caption to be appended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/captionreceiver/appendimmediately(_:)-9uy14)*