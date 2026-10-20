# currentSampleDuration

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The decode duration of the sample at the current position.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var currentSampleDuration: CMTime { get }
```

```objc
@property (nonatomic, readonly) CMTime currentSampleDuration;
```

#### Discussion

This value is [`indefinite`](../../CoreMedia/cmtime/indefinite.md) if the system needs to advance the sample past its current position to determine the decode duration. This can occur with streaming formats such as MPEG-2 transport streams.

## See Also

### Inspecting a sample cursor
- [var presentationTimeStamp: CMTime](./presentationtimestamp.md)
  The presentation timestamp (PTS) of the sample at the current position of the cursor.
- [var decodeTimeStamp: CMTime](./decodetimestamp.md)
  The decode timestamp (DTS) of the sample at the current position of the cursor.
- [var currentSampleFormatDescription: CMFormatDescription?](./currentsampleformatdescription.md)
  The format description for the sample at the current position of the cursor.
- [var syncInfo: AVSampleCursorSyncInfo](./syncinfo.md)
  Decoder synchronization information about the sample the cursor points to.
- [var dependencyInfo: AVSampleCursorDependencyInfo](./dependencyinfo.md)
  Dependency information about the sample the cursor points to.
- [var hevcDependencyInfo: MEHEVCDependencyInfo](./hevcdependencyinfo.md)
  Additional information that’s necessary to recover complete sample dependency information.
- [var decodeTimeOfLastSampleReachableByForwardSteppingThatIsAlreadyLoadedByByteSource: CMTime](./decodetimeoflastsamplereachablebyforwardsteppingthatisalreadyloadedbybytesource.md)
  The duration of the playable content starting from the cursor position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursor/currentsampleduration)*