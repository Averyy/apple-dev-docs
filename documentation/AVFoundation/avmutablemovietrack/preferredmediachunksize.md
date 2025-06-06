# preferredMediaChunkSize

**Framework**: AVFoundation  
**Kind**: property

The maximum size to use for each chunk of sample data written to the file for file types that support media chunk duration.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var preferredMediaChunkSize: Int { get set }
```

#### Discussion

The total size of the samples in a chunk can be no greater than the preferred chunk size, or the size of a single sample if the single sample’s size is greater than the preferred chunk size. The default media chunk duration is `1024 * 1024` bytes. Setting a negative value for the chunk duration will cause an error.

A larger chunk size can result in fewer reads from the storage container, at the potential expense of a larger memory footprint.

## See Also

- [var preferredMediaChunkAlignment: Int](avmutablemovietrack/preferredmediachunkalignment.md)
  The boundary for media chunk alignment for file types that support media chunk alignment.
- [var preferredMediaChunkDuration: CMTime](avmutablemovietrack/preferredmediachunkduration.md)
  The maximum duration to use for each chunk of sample data written to the file for file types that support media chunk duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/preferredmediachunksize)*