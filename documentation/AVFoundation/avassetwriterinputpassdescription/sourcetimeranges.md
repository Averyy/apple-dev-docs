# sourceTimeRanges

**Framework**: AVFoundation  
**Kind**: property

An array of time ranges.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var sourceTimeRanges: [NSValue] { get }
```

#### Discussion

Each element in the array is an [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) object that wraps a [`CMTimeRange`](https://developer.apple.com/documentation/CoreMedia/CMTimeRange) structure that represents one source time range. The value of this property is suitable to pass to the [`reset(forReadingTimeRanges:)`](avassetreaderoutput/reset(forreadingtimeranges:).md) method of [`AVAssetReaderOutput`](avassetreaderoutput.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputpassdescription/sourcetimeranges)*