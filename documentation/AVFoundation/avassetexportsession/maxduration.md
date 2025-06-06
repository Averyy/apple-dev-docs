# maxDuration

**Framework**: AVFoundation  
**Kind**: property

Provides an estimate of the maximum duration of the exported media.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 9.0+

## Declaration

```swift
var maxDuration: CMTime { get }
```

## See Also

- [func estimateMaximumDuration(completionHandler: (CMTime, (any Error)?) -> Void)](avassetexportsession/estimatemaximumduration(completionhandler:).md)
  Starts estimating the maximum duration of the export while considering the asset, preset, and time range configuration of the export session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/maxduration)*