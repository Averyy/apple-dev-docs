# currentSampleFormatDescription

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The format description for the sample at the current position of the cursor.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var currentSampleFormatDescription: CMFormatDescription? { get }
```

```objc
@property (nonatomic, readonly, nullable) CMFormatDescriptionRef currentSampleFormatDescription;
```

## See Also

### Inspecting a sample cursor
- [var presentationTimeStamp: CMTime](./presentationtimestamp.md)
  The presentation timestamp (PTS) of the sample at the current position of the cursor.
- [var decodeTimeStamp: CMTime](./decodetimestamp.md)
  The decode timestamp (DTS) of the sample at the current position of the cursor.
- [var currentSampleDuration: CMTime](./currentsampleduration.md)
  The decode duration of the sample at the current position.
- [var syncInfo: AVSampleCursorSyncInfo](./syncinfo.md)
  Decoder synchronization information about the sample the cursor points to.
- [var dependencyInfo: AVSampleCursorDependencyInfo](./dependencyinfo.md)
  Dependency information about the sample the cursor points to.
- [var hevcDependencyInfo: MEHEVCDependencyInfo](./hevcdependencyinfo.md)
  Additional information that’s necessary to recover complete sample dependency information.
- [var decodeTimeOfLastSampleReachableByForwardSteppingThatIsAlreadyLoadedByByteSource: CMTime](./decodetimeoflastsamplereachablebyforwardsteppingthatisalreadyloadedbybytesource.md)
  The duration of the playable content starting from the cursor position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursor/currentsampleformatdescription)*