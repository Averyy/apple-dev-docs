# startReading()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Prepares the asset reader to start reading sample buffers from the asset.

**Availability**:
- iOS 4.1+ - Deprecated in 27.0
- iPadOS 4.1+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.7+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use start() instead

## Declaration

```swift
func startReading() -> Bool
```

```objc
- (BOOL) startReading;
```

#### Return Value

`true` if the reader is able to start reading; otherwise, `false`.

#### Discussion

If this method returns `false`, you can determine the reason by checking the values of the [`status`](./status-swift.property.md) and [`error`](./error.md) properties.

## See Also

### Controlling reading
- [func start() throws](./start%28%29.md)
  Prepares the reader to read media data from the asset.
- [func cancelReading()](./cancelreading%28%29.md)
  Cancels any background work and stops the reader’s outputs from reading more samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreader/startreading())*