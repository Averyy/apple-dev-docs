# decodeTimeStamp

**Framework**: MediaExtension  
**Kind**: property  
**Required**: Yes

The decode timestamp (DTS) of the sample at the current position of the cursor.

**Availability**:
- macOS 14.0+

## Declaration

```swift
var decodeTimeStamp: CMTime { get }
```

## See Also

- [var presentationTimeStamp: CMTime](mesamplecursor/presentationtimestamp.md)
  The presentation timestamp (PTS) of the sample at the current position of the cursor.
- [var currentSampleDuration: CMTime](mesamplecursor/currentsampleduration.md)
  The decode duration of the sample at the current position.
- [var currentSampleFormatDescription: CMFormatDescription?](mesamplecursor/currentsampleformatdescription.md)
  The format description for the sample at the current position of the cursor.
- [var syncInfo: AVSampleCursorSyncInfo](mesamplecursor/syncinfo.md)
  Decoder synchronization information about the sample the cursor points to.
- [var dependencyInfo: AVSampleCursorDependencyInfo](mesamplecursor/dependencyinfo.md)
  Dependency information about the sample the cursor points to.
- [var hevcDependencyInfo: MEHEVCDependencyInfo](mesamplecursor/hevcdependencyinfo.md)
  Additional information that’s necessary to recover complete sample dependency information.
- [var decodeTimeOfLastSampleReachableByForwardSteppingThatIsAlreadyLoadedByByteSource: CMTime](mesamplecursor/decodetimeoflastsamplereachablebyforwardsteppingthatisalreadyloadedbybytesource.md)
  The duration of the playable content starting from the cursor position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursor/decodetimestamp)*