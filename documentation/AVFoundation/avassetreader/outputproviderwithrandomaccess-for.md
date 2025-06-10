# outputProviderWithRandomAccess(for:)

**Framework**: AVFoundation  
**Kind**: method

Attaches the output to the reader and returns a tuple with an output provider for reading sample buffers, and an associated random access controller.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func outputProviderWithRandomAccess(for output: AVAssetReaderOutput) -> sending (AVAssetReaderOutput.Provider<CMReadySampleBuffer<CMSampleBuffer.DynamicContent>>, AVAssetReaderOutput.RandomAccessController)
```

#### Return Value

A tuple with an output provider for reading sample buffers, and an associated random access controller.

## Parameters

- `output`: The output to be attached to the reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/outputproviderwithrandomaccess(for:))*