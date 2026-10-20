# FSVolume.CaseFormat

**Framework**: FSKit  
**Kind**: enum  
**Role**: Enumeration

An enumeration of case-sensitivity support types.

**Availability**:
- macOS 15.4+

## Declaration

```swift
enum CaseFormat
```

```c
enum FSVolumeCaseFormat : NSInteger;
```

#### Overview

A case-sensitive volume is a volume that treats upper and lower case characters in file and directory names as being distinct from each other. For example, `FILE.TXT` and `file.TXT` are different names in a case-sensitive volume, and the same name in a case-insensitive volume.

## Topics

### Declaring case formats
- [FSVolume.CaseFormat.sensitive](./caseformat/sensitive.md)
  The volume is case sensitive.
- [FSVolume.CaseFormat.insensitive](./caseformat/insensitive.md)
  The volume isn’t case sensitive.
- [FSVolume.CaseFormat.insensitiveCasePreserving](./caseformat/insensitivecasepreserving.md)
  The volume isn’t case sensitive, but supports preserving the case of file and directory names.
### Initializers
- [init?(rawValue: Int)](./caseformat/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Working with case sensitivity
- [var caseFormat: FSVolume.CaseFormat](./supportedcapabilities/caseformat.md)
  A value that indicates the volume’s support for case sensitivity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/caseformat)*