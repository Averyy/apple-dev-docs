# estimateMaximumDuration(completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Starts estimating the maximum duration of the export while considering the asset, preset, and time range configuration of the export session.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var estimatedMaximumDuration: CMTime { get async throws }
```

## Parameters

- `handler`: A callback the system invokes when it finishes its estimation. It passes the callback the following parameters:

## See Also

- [var maxDuration: CMTime](avassetexportsession/maxduration.md)
  Provides an estimate of the maximum duration of the exported media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/estimatemaximumduration(completionhandler:))*