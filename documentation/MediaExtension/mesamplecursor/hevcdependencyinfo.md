# hevcDependencyInfo

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

Additional information that’s necessary to recover complete sample dependency information.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@NSCopying
optional var hevcDependencyInfo: MEHEVCDependencyInfo { get }
```

```objc
@property (nonatomic, copy, readonly) MEHEVCDependencyInfo * hevcDependencyInfo;
```

## Discussion

This is an optional property that provides additional sample dependency information that [`syncInfo`](./syncinfo.md) and [`dependencyInfo`](./dependencyinfo.md) don’t provide. Examples of this are the NAL unit type of an HEVC sync sample or the number of samples necessary to refresh the decoder after a USAC independent frame. Don’t implement this property for formats where this information doesn’t make sense.

## See Also

### Inspecting a sample cursor
- [var presentationTimeStamp: CMTime](./presentationtimestamp.md)
  The presentation timestamp (PTS) of the sample at the current position of the cursor.
- [var decodeTimeStamp: CMTime](./decodetimestamp.md)
  The decode timestamp (DTS) of the sample at the current position of the cursor.
- [var currentSampleDuration: CMTime](./currentsampleduration.md)
  The decode duration of the sample at the current position.
- [var currentSampleFormatDescription: CMFormatDescription?](./currentsampleformatdescription.md)
  The format description for the sample at the current position of the cursor.
- [var syncInfo: AVSampleCursorSyncInfo](./syncinfo.md)
  Decoder synchronization information about the sample the cursor points to.
- [var dependencyInfo: AVSampleCursorDependencyInfo](./dependencyinfo.md)
  Dependency information about the sample the cursor points to.
- [var decodeTimeOfLastSampleReachableByForwardSteppingThatIsAlreadyLoadedByByteSource: CMTime](./decodetimeoflastsamplereachablebyforwardsteppingthatisalreadyloadedbybytesource.md)
  The duration of the playable content starting from the cursor position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursor/hevcdependencyinfo)*