# hevcDependencyInfo

**Framework**: MediaExtension  
**Kind**: property

Additional information that’s necessary to recover complete sample dependency information.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@NSCopying
optional var hevcDependencyInfo: MEHEVCDependencyInfo { get }
```

#### Discussion

This is an optional property that provides additional sample dependency information that [`syncInfo`](mesamplecursor/syncinfo.md) and [`dependencyInfo`](mesamplecursor/dependencyinfo.md) don’t provide. Examples of this are the NAL unit type of an HEVC sync sample or the number of samples necessary to refresh the decoder after a USAC independent frame. Don’t implement this property for formats where this information doesn’t make sense.

## See Also

- [var presentationTimeStamp: CMTime](mesamplecursor/presentationtimestamp.md)
  The presentation timestamp (PTS) of the sample at the current position of the cursor.
- [var decodeTimeStamp: CMTime](mesamplecursor/decodetimestamp.md)
  The decode timestamp (DTS) of the sample at the current position of the cursor.
- [var currentSampleDuration: CMTime](mesamplecursor/currentsampleduration.md)
  The decode duration of the sample at the current position.
- [var currentSampleFormatDescription: CMFormatDescription?](mesamplecursor/currentsampleformatdescription.md)
  The format description for the sample at the current position of the cursor.
- [var syncInfo: AVSampleCursorSyncInfo](mesamplecursor/syncinfo.md)
  Decoder synchronization information about the sample the cursor points to.
- [var dependencyInfo: AVSampleCursorDependencyInfo](mesamplecursor/dependencyinfo.md)
  Dependency information about the sample the cursor points to.
- [var decodeTimeOfLastSampleReachableByForwardSteppingThatIsAlreadyLoadedByByteSource: CMTime](mesamplecursor/decodetimeoflastsamplereachablebyforwardsteppingthatisalreadyloadedbybytesource.md)
  The duration of the playable content starting from the cursor position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursor/hevcdependencyinfo)*