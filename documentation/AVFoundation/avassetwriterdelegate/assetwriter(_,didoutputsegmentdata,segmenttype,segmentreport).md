# assetWriter(_:didOutputSegmentData:segmentType:segmentReport:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) assetWriter:(AVAssetWriter *) writer didOutputSegmentData:(NSData *) segmentData segmentType:(AVAssetSegmentType) segmentType segmentReport:(AVAssetSegmentReport *) segmentReport;
```

## Discussion

The asset writer stops normal file writing when you implement this method.

## Parameters

- `writer`: The asset writer that output segment data.
- `segmentData`: The data for the segment.
- `segmentType`: The type of segment data.
- `segmentReport`: A report for the segment data.

## See Also

### Responding to segment output
- [func assetWriter(AVAssetWriter, didOutputSegmentData: Data, segmentType: AVAssetSegmentType)](./assetwriter%28_,didoutputsegmentdata,segmenttype%29.md)
  Tells the delegate that the asset writer output segment data.
- [class AVAssetSegmentReport](../avassetsegmentreport.md)
  An object that provides information about segment data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterdelegate/assetwriter(_:didoutputsegmentdata:segmenttype:segmentreport:))*