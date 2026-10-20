# supportedVolumeCapabilities

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

**Availability**:
- macOS 27.0+

## Declaration

```swift
var supportedVolumeCapabilities: FSVolume.SupportedCapabilities { get }
```

```objc
@property (nonatomic, readonly) FSVolumeSupportedCapabilities * supportedVolumeCapabilities;
```

## See Also

### Inspecting required volume properties
- [FSVolume.SupportedCapabilities](../supportedcapabilities.md)
  A type that represents capabilities supported by a volume, such as hard and symbolic links, journaling, and large file sizes.
- [var volumeStatistics: FSStatFSResult](./volumestatistics.md)
  A property that provides up-to-date statistics of the volume.
- [class FSStatFSResult](../../fsstatfsresult.md)
  A type used to report a volume’s statistics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/handler/supportedvolumecapabilities)*