# decodeTimeOfLastSampleReachableByForwardSteppingThatIsAlreadyLoadedByByteSource

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

The duration of the playable content starting from the cursor position.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional var decodeTimeOfLastSampleReachableByForwardSteppingThatIsAlreadyLoadedByByteSource: CMTime { get }
```

```objc
@property (nonatomic, readonly) CMTime decodeTimeOfLastSampleReachableByForwardSteppingThatIsAlreadyLoadedByByteSource;
```

## Discussion

Indicates the time difference between the current cursor decode timestamp (DTS) and the last reachable sample DTS. This is necessary to play certain assets such as those with HTTP URLs, because it indicates what samples the byte source has already loaded.

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
- [var hevcDependencyInfo: MEHEVCDependencyInfo](./hevcdependencyinfo.md)
  Additional information that’s necessary to recover complete sample dependency information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursor/decodetimeoflastsamplereachablebyforwardsteppingthatisalreadyloadedbybytesource)*