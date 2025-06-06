# kDADiskDescriptionWatchVolumePath

**Framework**: Disk Arbitration  
**Kind**: var

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
var kDADiskDescriptionWatchVolumePath: Unmanaged<CFArray>
```

#### Discussion

Predefined CFArray object containing a set of disk description keys appropriate for watching volume mount changes using DARegisterDiskDescriptionChangedCallback().

## See Also

- [var kDADiskDescriptionMatchMediaUnformatted: Unmanaged<CFDictionary>](kdadiskdescriptionmatchmediaunformatted.md)
- [var kDADiskDescriptionMatchMediaWhole: Unmanaged<CFDictionary>](kdadiskdescriptionmatchmediawhole.md)
- [var kDADiskDescriptionMatchVolumeMountable: Unmanaged<CFDictionary>](kdadiskdescriptionmatchvolumemountable.md)
- [var kDADiskDescriptionMatchVolumeUnrecognized: Unmanaged<CFDictionary>](kdadiskdescriptionmatchvolumeunrecognized.md)
- [var kDADiskDescriptionWatchVolumeName: Unmanaged<CFArray>](kdadiskdescriptionwatchvolumename.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionwatchvolumepath)*