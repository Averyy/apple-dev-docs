# outputMetadataProvider(for:)

**Framework**: AVFoundation  
**Kind**: method

Attaches the output to the reader and returns an output provider for reading timed metadata groups.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func outputMetadataProvider(for output: AVAssetReaderTrackOutput) -> sending AVAssetReaderOutput.Provider<AVTimedMetadataGroup>
```

#### Return Value

A reader output provider with an interface for reading timed metadata groups.

## Parameters

- `output`: The output to be attached to the reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/outputmetadataprovider(for:))*