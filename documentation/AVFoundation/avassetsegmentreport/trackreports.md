# trackReports

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The reports for the segment’s track data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var trackReports: [AVAssetSegmentTrackReport] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVAssetSegmentTrackReport *> * trackReports;
```

## See Also

### Inspecting a report
- [var segmentType: AVAssetSegmentType](./segmenttype.md)
  The type of segment data.
- [enum AVAssetSegmentType](../avassetsegmenttype.md)
  Constants that define the type of a segment.
- [class AVAssetSegmentTrackReport](../avassetsegmenttrackreport.md)
  An object that provides information on a track in segment data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetsegmentreport/trackreports)*