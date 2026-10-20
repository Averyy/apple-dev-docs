# volumeStatistics

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A property that provides up-to-date statistics of the volume.

**Availability**:
- macOS 27.0+

## Declaration

```swift
var volumeStatistics: FSStatFSResult { get }
```

```objc
@property (nonatomic, readonly) FSStatFSResult * volumeStatistics;
```

## See Also

### Inspecting required volume properties
- [var supportedVolumeCapabilities: FSVolume.SupportedCapabilities](./supportedvolumecapabilities.md)
- [FSVolume.SupportedCapabilities](../supportedcapabilities.md)
  A type that represents capabilities supported by a volume, such as hard and symbolic links, journaling, and large file sizes.
- [class FSStatFSResult](../../fsstatfsresult.md)
  A type used to report a volume’s statistics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/handler/volumestatistics)*