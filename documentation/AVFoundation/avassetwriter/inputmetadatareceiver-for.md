# inputMetadataReceiver(for:)

**Framework**: AVFoundation  
**Kind**: method

Attaches the input to the writer and returns an input receiver for writing timed metadata group.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func inputMetadataReceiver(for input: AVAssetWriterInput) -> sending AVAssetWriterInput.MetadataReceiver
```

#### Return Value

A writer input receiver with an interface for writing timed metadata group.

## Parameters

- `input`: The input to be attached to the writer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriter/inputmetadatareceiver(for:))*