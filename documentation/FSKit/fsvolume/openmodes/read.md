# read

**Framework**: FSKit  
**Kind**: property  
**Role**: Type Property

The read mode.

**Availability**:
- macOS 15.4+

## Declaration

```swift
static var read: FSVolume.OpenModes { get }
```

```c
FSVolumeOpenModesRead
```

#### Discussion

This mode is equivalent to POSIX `FREAD`.

## See Also

### Declaring open modes
- [static var write: FSVolume.OpenModes](./write.md)
  The write mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/openmodes/read)*