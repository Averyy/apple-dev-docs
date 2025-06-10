# appendImmediately(_:with:)

**Framework**: AVFoundation  
**Kind**: method

Appends the tagged pixel buffers synchronously if the input is ready for more media data.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func appendImmediately(_ taggedPixelBufferGroup: [CMTaggedDynamicBuffer], with presentationTime: CMTime) throws -> Bool
```

#### Return Value

Returns true if the append was successful, false if the input was not ready for more media data.

#### Discussion

> **Note**: An error if the underlying writer failed.

## Parameters

- `taggedPixelBufferGroup`: The tagged pixel buffers to be appended.
- `presentationTime`: The presentation time for the tagged pixel buffers to be appended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver/appendimmediately(_:with:))*