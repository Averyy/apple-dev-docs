# kDADiskDescriptionMatchMediaWhole

**Framework**: Disk Arbitration  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
var kDADiskDescriptionMatchMediaWhole: Unmanaged<CFDictionary>
```

```c
extern CFDictionaryRef kDADiskDescriptionMatchMediaWhole;
```

## Discussion

Predefined CFDictionary object containing a set of disk description keys and values appropriate for matching whole media using DARegister*Callback().

## See Also

### Constants
- [var kDADiskDescriptionMatchMediaUnformatted: Unmanaged<CFDictionary>](./kdadiskdescriptionmatchmediaunformatted.md)
- [var kDADiskDescriptionMatchVolumeMountable: Unmanaged<CFDictionary>](./kdadiskdescriptionmatchvolumemountable.md)
- [var kDADiskDescriptionMatchVolumeUnrecognized: Unmanaged<CFDictionary>](./kdadiskdescriptionmatchvolumeunrecognized.md)
- [var kDADiskDescriptionWatchVolumeName: Unmanaged<CFArray>](./kdadiskdescriptionwatchvolumename.md)
- [var kDADiskDescriptionWatchVolumePath: Unmanaged<CFArray>](./kdadiskdescriptionwatchvolumepath.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/kdadiskdescriptionmatchmediawhole)*