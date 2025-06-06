# CMBufferGetSizeCallback

**Framework**: Core Media  
**Kind**: typealias

A client callback that returns a size.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
typealias CMBufferGetSizeCallback = (CMBuffer, UnsafeMutableRawPointer?) -> Int
```

## Parameters

- `buf`: The buffer being interrogated.
- `refcon`: The client refcon. Can be  .

## See Also

- [class CMSampleBuffer](cmsamplebuffer.md)
  A reference to a buffer of media data.
- [Sample Buffer Flags](sample-buffer-flags.md)
  Flags that customize the behavior of framework operations.
- [struct CMSampleTimingInfo](cmsampletiminginfo.md)
  A collection of timing information for a sample in a sample buffer.
- [typealias CMBuffer](cmbuffer.md)
  A reference to a buffer object.
- [typealias CMItemIndex](cmitemindex.md)
  A datatype that represents an item index.
- [typealias CMItemCount](cmitemcount.md)
  A datatype that represents an item count.
- [typealias CMPersistentTrackID](cmpersistenttrackid.md)
  A datatype that represents a persistent track identifier.
- [typealias CMMuxedStreamType](cmmuxedstreamtype.md)
  A datatype that represents a muxed stream of data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbuffergetsizecallback)*