# CMTimeMapping

**Framework**: Core Media

A structure that maps a segment of a source time range to a target time range.

## Topics

### Creating Time Mappings
- [func CMTimeMappingMake(source: CMTimeRange, target: CMTimeRange) -> CMTimeMapping](cmtimemappingmake(source:target:).md)
  Creates a time mapping with a source and target time range.
- [func CMTimeMappingMakeEmpty(target: CMTimeRange) -> CMTimeMapping](cmtimemappingmakeempty(target:).md)
  Creates a valid time mapping with an empty source.
- [func CMTimeMappingMakeFromDictionary(CFDictionary) -> CMTimeMapping](cmtimemappingmakefromdictionary(_:).md)
  Creates a time mapping from a dictionary representation.
### Representing Time Mappings
- [func CMTimeMappingCopyAsDictionary(CMTimeMapping, allocator: CFAllocator?) -> CFDictionary?](cmtimemappingcopyasdictionary(_:allocator:).md)
  Returns a dictionary representation of a time mapping.
- [func CMTimeMappingCopyDescription(allocator: CFAllocator?, mapping: CMTimeMapping) -> CFString?](cmtimemappingcopydescription(allocator:mapping:).md)
  Copies a string description of a time mapping.
- [func CMTimeMappingShow(CMTimeMapping)](cmtimemappingshow(_:).md)
  Prints a description of a time mapping to standard output.
### Data Types
- [struct CMTimeMapping](cmtimemapping.md)
  A structure that maps a segment of a source time range to a target time range.
### Constants
- [static let invalid: CMTimeMapping](cmtimemapping/invalid.md)
  An invalid time mapping.
- [let kCMTimeMappingSourceKey: CFString](kcmtimemappingsourcekey.md)
  A dictionary key for a source time range.
- [let kCMTimeMappingTargetKey: CFString](kcmtimemappingtargetkey.md)
  A dictionary key for a target time range.

## See Also

- [CMTime](cmtime-api.md)
  A structure that represents time.
- [CMTimeRange](cmtimerange-api.md)
  A structure that represents a range of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimemapping-api)*