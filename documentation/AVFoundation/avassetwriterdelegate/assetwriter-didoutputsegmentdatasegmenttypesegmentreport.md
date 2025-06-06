# assetWriter(_:didOutputSegmentData:segmentType:segmentReport:)

**Framework**: AVFoundation  
**Kind**: method

Tells the delegate that the asset writer output segment data and a report.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
optional func assetWriter(_ writer: AVAssetWriter, didOutputSegmentData segmentData: Data, segmentType: AVAssetSegmentType, segmentReport: AVAssetSegmentReport?)
```

#### Discussion

The asset writer stops normal file writing when you implement this method.

## Parameters

- `writer`: The asset writer that output segment data.
- `segmentData`: The data for the segment.
- `segmentType`: The type of segment data.
- `segmentReport`: A report for the segment data.

## See Also

- [func assetWriter(AVAssetWriter, didOutputSegmentData: Data, segmentType: AVAssetSegmentType)](avassetwriterdelegate/assetwriter(_:didoutputsegmentdata:segmenttype:).md)
  Tells the delegate that the asset writer output segment data.
- [class AVAssetSegmentReport](avassetsegmentreport.md)
  An object that provides information about segment data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterdelegate/assetwriter(_:didoutputsegmentdata:segmenttype:segmentreport:))*