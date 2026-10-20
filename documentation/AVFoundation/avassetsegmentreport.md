# AVAssetSegmentReport

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVAssetSegmentReport : NSObject
```

#### Overview

You receive a segment report through the [`assetWriter(_:didOutputSegmentData:segmentType:segmentReport:)`](./avassetwriterdelegate/assetwriter%28_,didoutputsegmentdata,segmenttype,segmentreport%29.md) delegate method.

## Topics

### Inspecting a report
- [var segmentType: AVAssetSegmentType](./avassetsegmentreport/segmenttype.md)
  The type of segment data.
- [enum AVAssetSegmentType](./avassetsegmenttype.md)
  Constants that define the type of a segment.
- [var trackReports: [AVAssetSegmentTrackReport]](./avassetsegmentreport/trackreports.md)
  The reports for the segment’s track data.
- [class AVAssetSegmentTrackReport](./avassetsegmenttrackreport.md)
  An object that provides information on a track in segment data.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Responding to segment output
- [func assetWriter(AVAssetWriter, didOutputSegmentData: Data, segmentType: AVAssetSegmentType)](./avassetwriterdelegate/assetwriter%28_,didoutputsegmentdata,segmenttype%29.md)
  Tells the delegate that the asset writer output segment data.
- [func assetWriter(AVAssetWriter, didOutputSegmentData: Data, segmentType: AVAssetSegmentType, segmentReport: AVAssetSegmentReport?)](./avassetwriterdelegate/assetwriter%28_,didoutputsegmentdata,segmenttype,segmentreport%29.md)
  Tells the delegate that the asset writer output segment data and a report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetsegmentreport)*