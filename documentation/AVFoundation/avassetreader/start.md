# start()

**Framework**: AVFoundation  
**Kind**: method

Prepares the reader to read media data from the asset.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func start() throws
```

#### Discussion

> **Note**: An error if reading fails to start.

## See Also

- [func startReading() -> Bool](avassetreader/startreading.md)
  Prepares the asset reader to start reading sample buffers from the asset.
- [func cancelReading()](avassetreader/cancelreading.md)
  Cancels any background work and stops the reader’s outputs from reading more samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/start())*