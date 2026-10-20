# syncInfo

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

Decoder synchronization information about the sample the cursor points to.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional var syncInfo: AVSampleCursorSyncInfo { get }
```

```objc
@property (nonatomic, readonly) AVSampleCursorSyncInfo syncInfo;
```

#### Discussion

This value includes any valid flags set. Don’t implement this property if this kind of synchronization information doesn’t make sense for the sequence of samples.

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
- [var dependencyInfo: AVSampleCursorDependencyInfo](./dependencyinfo.md)
  Dependency information about the sample the cursor points to.
- [var hevcDependencyInfo: MEHEVCDependencyInfo](./hevcdependencyinfo.md)
  Additional information that’s necessary to recover complete sample dependency information.
- [var decodeTimeOfLastSampleReachableByForwardSteppingThatIsAlreadyLoadedByByteSource: CMTime](./decodetimeoflastsamplereachablebyforwardsteppingthatisalreadyloadedbybytesource.md)
  The duration of the playable content starting from the cursor position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mesamplecursor/syncinfo)*