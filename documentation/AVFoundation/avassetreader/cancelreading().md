# cancelReading()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Cancels any background work and stops the reader’s outputs from reading more samples.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func cancelReading()
```

```objc
- (void) cancelReading;
```

## Discussion

To stop reading samples before reaching the end of the time range, call this method to stop any in-progress background read operations.

## See Also

### Controlling reading
- [func start() throws](./start%28%29.md)
  Prepares the reader to read media data from the asset.
- [func startReading() -> Bool](./startreading%28%29.md)
  Prepares the asset reader to start reading sample buffers from the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/cancelreading())*