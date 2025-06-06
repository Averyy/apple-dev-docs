# dependencyInfo

**Framework**: MediaExtension  
**Kind**: property

Dependency information about the sample the cursor points to.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional var dependencyInfo: AVSampleCursorDependencyInfo { get }
```

#### Discussion

This value includes any valid flags set. Don’t implement this property if this kind of dependency information doesn’t make sense for the sequence of samples.

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
- [var hevcDependencyInfo: MEHEVCDependencyInfo](mesamplecursor/hevcdependencyinfo.md)
  Additional information that’s necessary to recover complete sample dependency information.
- [var decodeTimeOfLastSampleReachableByForwardSteppingThatIsAlreadyLoadedByByteSource: CMTime](mesamplecursor/decodetimeoflastsamplereachablebyforwardsteppingthatisalreadyloadedbybytesource.md)
  The duration of the playable content starting from the cursor position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursor/dependencyinfo)*