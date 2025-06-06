# FSVolume.CaseFormat

**Framework**: FSKit  
**Kind**: enum

An enumeration of case-sensitivity support types.

**Availability**:
- macOS 15.4+

## Declaration

```swift
enum CaseFormat
```

#### Overview

A case-sensitive volume is a volume that treats upper and lower case characters in file and directory names as being distinct from each other. For example, `FILE.TXT` and `file.TXT` are different names in a case-sensitive volume, and the same name in a case-insensitive volume.

## Topics

### Declaring case formats
- [FSVolume.CaseFormat.sensitive](fsvolume/caseformat/sensitive.md)
  The volume is case sensitive.
- [FSVolume.CaseFormat.insensitive](fsvolume/caseformat/insensitive.md)
  The volume isn’t case sensitive.
- [FSVolume.CaseFormat.insensitiveCasePreserving](fsvolume/caseformat/insensitivecasepreserving.md)
  The volume isn’t case sensitive, but supports preserving the case of file and directory names.
### Initializers
- [init?(rawValue: Int)](fsvolume/caseformat/init(rawvalue:).md)
### Default Implementations
- [Equatable Implementations](fsvolume/caseformat/equatable-implementations.md)
- [RawRepresentable Implementations](fsvolume/caseformat/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var caseFormat: FSVolume.CaseFormat](fsvolume/supportedcapabilities/caseformat.md)
  A value that indicates the volume’s support for case sensitivity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/caseformat)*