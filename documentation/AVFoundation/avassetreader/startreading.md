# startReading()

**Framework**: AVFoundation  
**Kind**: method

Prepares the asset reader to start reading sample buffers from the asset.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func startReading() -> Bool
```

#### Return Value

`true` if the reader is able to start reading; otherwise, `false`.

#### Discussion

If this method returns `false`, you can determine the reason by checking the values of the [`status`](avassetreader/status-swift.property.md) and [`error`](avassetreader/error.md) properties.

## See Also

- [func start() throws](avassetreader/start.md)
  Prepares the reader to read media data from the asset.
- [func cancelReading()](avassetreader/cancelreading.md)
  Cancels any background work and stops the reader’s outputs from reading more samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/startreading())*