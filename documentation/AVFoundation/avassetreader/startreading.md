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

[`true`](https://developer.apple.com/documentation/swift/true) if the reader is able to start reading; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

If this method returns [`false`](https://developer.apple.com/documentation/swift/false), you can determine the reason by checking the values of the [`status`](avassetreader/status-swift.property.md) and [`error`](avassetreader/error.md) properties.

## See Also

- [func cancelReading()](avassetreader/cancelreading.md)
  Cancels any background work and stops the reader’s outputs from reading more samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/startreading())*