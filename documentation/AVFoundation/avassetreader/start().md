# start()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Prepares the reader to read media data from the asset.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func start() throws
```

#### Discussion

> **Throws**: An error if reading fails to start.

## See Also

### Controlling reading
- [func startReading() -> Bool](./startreading%28%29.md)
  Prepares the asset reader to start reading sample buffers from the asset.
- [func cancelReading()](./cancelreading%28%29.md)
  Cancels any background work and stops the reader’s outputs from reading more samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/start())*