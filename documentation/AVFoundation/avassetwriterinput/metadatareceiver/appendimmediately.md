# appendImmediately(_:)

**Framework**: AVFoundation  
**Kind**: method

Appends the timed metadata group synchronously if the input is ready for more media data.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func appendImmediately(_ timedMetadataGroup: AVTimedMetadataGroup) throws -> Bool
```

#### Return Value

Returns true if the append was successful, false if the input was not ready for more media data.

#### Discussion

> **Note**: An error if the underlying writer failed.

## Parameters

- `timedMetadataGroup`: The timed metadata group to be appended


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput/metadatareceiver/appendimmediately(_:))*