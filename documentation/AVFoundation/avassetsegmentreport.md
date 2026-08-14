# AVAssetSegmentReport

**Framework**: AVFoundation  
**Kind**: class

An object that provides information about segment data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class AVAssetSegmentReport
```

#### Overview

You receive a segment report through the [`assetWriter(_:didOutputSegmentData:segmentType:segmentReport:)`](avassetwriterdelegate/assetwriter(_:didoutputsegmentdata:segmenttype:segmentreport:).md) delegate method.

## Topics

### Inspecting a report
- [var segmentType: AVAssetSegmentType](avassetsegmentreport/segmenttype.md)
  The type of segment data.
- [enum AVAssetSegmentType](avassetsegmenttype.md)
  Constants that define the type of a segment.
- [var trackReports: [AVAssetSegmentTrackReport]](avassetsegmentreport/trackreports.md)
  The reports for the segment’s track data.
- [class AVAssetSegmentTrackReport](avassetsegmenttrackreport.md)
  An object that provides information on a track in segment data.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func assetWriter(AVAssetWriter, didOutputSegmentData: Data, segmentType: AVAssetSegmentType)](avassetwriterdelegate/assetwriter(_:didoutputsegmentdata:segmenttype:).md)
  Tells the delegate that the asset writer output segment data.
- [func assetWriter(AVAssetWriter, didOutputSegmentData: Data, segmentType: AVAssetSegmentType, segmentReport: AVAssetSegmentReport?)](avassetwriterdelegate/assetwriter(_:didoutputsegmentdata:segmenttype:segmentreport:).md)
  Tells the delegate that the asset writer output segment data and a report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetsegmentreport)*