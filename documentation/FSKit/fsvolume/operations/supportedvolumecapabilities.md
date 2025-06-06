# supportedVolumeCapabilities

**Framework**: FSKit  
**Kind**: property  
**Required**: Yes

A property that provides the supported capabilities of the volume.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var supportedVolumeCapabilities: FSVolume.SupportedCapabilities { get }
```

## See Also

- [FSVolume.SupportedCapabilities](fsvolume/supportedcapabilities.md)
  A type that represents capabillities supported by a volume, such as hard and symbolic links, journaling, and large file sizes.
- [var volumeStatistics: FSStatFSResult](fsvolume/operations/volumestatistics.md)
  A property that provides up-to-date statistics of the volume.
- [class FSStatFSResult](fsstatfsresult.md)
  A type used to report a volume’s statistics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/supportedvolumecapabilities)*