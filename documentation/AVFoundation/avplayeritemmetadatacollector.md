# AVPlayerItemMetadataCollector

**Framework**: AVFoundation  
**Kind**: class

An object used to capture the date range metadata defined for an HTTP Live Streaming asset.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.11.3+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 2.3+

## Declaration

```swift
class AVPlayerItemMetadataCollector
```

#### Overview

You can use the HLS `#EXT-X-DATERANGE` tag to define date range metadata in a media playlist. This tag is useful for defining timed metadata for interstitial regions such as advertisements, but can be used to define any timed metadata needed by your stream. To access this metadata when the stream is played using an [`AVPlayer`](avplayer.md), you create an instance of `AVPlayerItemMetadataCollector`, configure its delegate object (see [`AVPlayerItemMetadataCollectorPushDelegate`](avplayeritemmetadatacollectorpushdelegate.md)), and add it as a media data collector to the [`AVPlayerItem`](avplayeritem.md) (see example).

Creating an `AVPlayerItemMetadataCollector` as shown in the example, will capture all `#EXT-X-DATERANGE` metadata defined in your stream. If you would like to filter the output to only the metadata of interest, you can create an instance to filter by identifier and/or classifying labels using the [`init(identifiers:classifyingLabels:)`](avplayeritemmetadatacollector/init(identifiers:classifyinglabels:).md) initializer.

## Topics

### Creating a Metadata Collector
- [init(identifiers: [String]?, classifyingLabels: [String]?)](avplayeritemmetadatacollector/init(identifiers:classifyinglabels:).md)
  Creates a metadata collector to access a stream’s metadata groups matching the specified array of identifiers and classifying labels.
### Accessing the Delegate and Callback Queue
- [func setDelegate((any AVPlayerItemMetadataCollectorPushDelegate)?, queue: dispatch_queue_t?)](avplayeritemmetadatacollector/setdelegate(_:queue:).md)
  Sets the delegate and a dispatch queue on which the delegate will be called.
- [var delegate: (any AVPlayerItemMetadataCollectorPushDelegate)?](avplayeritemmetadatacollector/delegate.md)
  Accesses the metadata collector’s delegate object.
- [protocol AVPlayerItemMetadataCollectorPushDelegate](avplayeritemmetadatacollectorpushdelegate.md)
  A protocol you implement to receive metadata callbacks from a player item metadata collector.
- [var delegateQueue: dispatch_queue_t?](avplayeritemmetadatacollector/delegatequeue.md)
  The dispatch queue on which the delegate’s methods are called.

## Relationships

### Inherits From
- [AVPlayerItemMediaDataCollector](avplayeritemmediadatacollector.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Presenting Chapter Markers](presenting-chapter-markers.md)
  Add chapter markers to enable users to quickly navigate your content.
- [class AVMetadataGroup](avmetadatagroup.md)
  A collection of metadata items associated with a timeline segment.
- [class AVTimedMetadataGroup](avtimedmetadatagroup.md)
  A collection of metadata items that are valid for use during a specific time range.
- [class AVMutableTimedMetadataGroup](avmutabletimedmetadatagroup.md)
  A mutable collection of metadata items that are valid for use during a specific time range.
- [class AVDateRangeMetadataGroup](avdaterangemetadatagroup.md)
  A collection of metadata items that are valid for use within a specific date range.
- [class AVMutableDateRangeMetadataGroup](avmutabledaterangemetadatagroup.md)
  A mutable collection of metadata items that are valid for use within a specific range of dates.
- [class AVPlayerItemMediaDataCollector](avplayeritemmediadatacollector.md)
  The abstract base for media data collectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollector)*