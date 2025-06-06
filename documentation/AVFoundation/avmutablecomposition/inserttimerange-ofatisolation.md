# insertTimeRange(_:of:at:isolation:)

**Framework**: AVFoundation  
**Kind**: method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@backDeployed(before: macOS 15, iOS 18, tvOS 18, watchOS 11, visionOS 2)
final func insertTimeRange(_ timeRange: CMTimeRange, of asset: AVAsset, at time: CMTime, isolation: isolated (any Actor)? = #isolation) async throws
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecomposition/inserttimerange(_:of:at:isolation:))*