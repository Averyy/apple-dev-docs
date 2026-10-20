# AVAssetWriterDelegate

**Framework**: AVFoundation  
**Kind**: protocol  
**Role**: Protocol

A delegate protocol that defines the methods to implement to respond to asset-writing events.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
protocol AVAssetWriterDelegate : NSObjectProtocol, Sendable
```

```objc
@protocol AVAssetWriterDelegate <NSObject>
```

## Topics

### Responding to segment output
- [func assetWriter(AVAssetWriter, didOutputSegmentData: Data, segmentType: AVAssetSegmentType)](./avassetwriterdelegate/assetwriter%28_,didoutputsegmentdata,segmenttype%29.md)
  Tells the delegate that the asset writer output segment data.
- [func assetWriter(AVAssetWriter, didOutputSegmentData: Data, segmentType: AVAssetSegmentType, segmentReport: AVAssetSegmentReport?)](./avassetwriterdelegate/assetwriter%28_,didoutputsegmentdata,segmenttype,segmentreport%29.md)
  Tells the delegate that the asset writer output segment data and a report.
- [class AVAssetSegmentReport](./avassetsegmentreport.md)
  An object that provides information about segment data.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring segment writing
- [var delegate: (any AVAssetWriterDelegate)?](./avassetwriter/delegate.md)
  A delegate object that responds to asset-writing events.
- [var preferredOutputSegmentInterval: CMTime](./avassetwriter/preferredoutputsegmentinterval.md)
  The interval of output segments that you prefer.
- [var initialSegmentStartTime: CMTime](./avassetwriter/initialsegmentstarttime.md)
  The start time of the initial segment.
- [var outputFileTypeProfile: AVFileTypeProfile?](./avassetwriter/outputfiletypeprofile.md)
  A profile for the output file type.
- [func flushSegment()](./avassetwriter/flushsegment%28%29.md)
  Closes the current segment and outputs it to a delegate method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterdelegate)*