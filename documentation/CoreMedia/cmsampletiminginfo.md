# CMSampleTimingInfo

**Framework**: Core Media  
**Kind**: struct

A collection of timing information for a sample in a sample buffer.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct CMSampleTimingInfo
```

#### Overview

A single `CMSampleTimingInfo` struct can describe every individual sample in a `CMSampleBuffer`, if the samples all have the same duration and are in presentation order with no gaps.

## Topics

### Constants
- [static let invalid: CMSampleTimingInfo](cmsampletiminginfo/invalid.md)
### Initializers
- [init()](cmsampletiminginfo/init.md)
- [init(duration: CMTime, presentationTimeStamp: CMTime, decodeTimeStamp: CMTime)](cmsampletiminginfo/init(duration:presentationtimestamp:decodetimestamp:).md)
### Properties
- [var decodeTimeStamp: CMTime](cmsampletiminginfo/decodetimestamp.md)
  The time at which the sample will be decoded.
- [var duration: CMTime](cmsampletiminginfo/duration.md)
  The duration of the sample.
- [var presentationTimeStamp: CMTime](cmsampletiminginfo/presentationtimestamp.md)
  The time at which the sample will be presented.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class CMSampleBuffer](cmsamplebuffer.md)
  A reference to a buffer of media data.
- [Sample Buffer Flags](sample-buffer-flags.md)
  Flags that customize the behavior of framework operations.
- [typealias CMBuffer](cmbuffer.md)
  A reference to a buffer object.
- [typealias CMBufferGetSizeCallback](cmbuffergetsizecallback.md)
  A client callback that returns a size.
- [typealias CMItemIndex](cmitemindex.md)
  A datatype that represents an item index.
- [typealias CMItemCount](cmitemcount.md)
  A datatype that represents an item count.
- [typealias CMPersistentTrackID](cmpersistenttrackid.md)
  A datatype that represents a persistent track identifier.
- [typealias CMMuxedStreamType](cmmuxedstreamtype.md)
  A datatype that represents a muxed stream of data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsampletiminginfo)*