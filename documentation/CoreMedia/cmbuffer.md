# CMBuffer

**Framework**: Core Media  
**Kind**: typealias

A reference to a buffer object.

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
typealias CMBuffer = CFTypeRef
```

#### Discussion

A `CMBuffer` can be an instance of any Core Foundation type, as long as a `getDuration` callback can be provided. Commonly used types are `CMSampleBuffer` and `CVPixelBuffer`.

## See Also

- [class CMSampleBuffer](cmsamplebuffer.md)
  A reference to a buffer of media data.
- [Sample Buffer Flags](sample-buffer-flags.md)
  Flags that customize the behavior of framework operations.
- [struct CMSampleTimingInfo](cmsampletiminginfo.md)
  A collection of timing information for a sample in a sample buffer.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbuffer)*