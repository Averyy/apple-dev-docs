# CMTimeMappingShow(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Prints a description of a time mapping to standard output.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMTimeMappingShow(_ mapping: CMTimeMapping)
```

```c
extern void CMTimeMappingShow(CMTimeMapping mapping);
```

#### Discussion

You typically use this function for debugging purposes.

## Parameters

- `mapping`: The time mapping to show.

## See Also

### Representing Time Mappings
- [func CMTimeMappingCopyAsDictionary(CMTimeMapping, allocator: CFAllocator?) -> CFDictionary?](./cmtimemappingcopyasdictionary%28_,allocator%29.md)
  Returns a dictionary representation of a time mapping.
- [func CMTimeMappingCopyDescription(allocator: CFAllocator?, mapping: CMTimeMapping) -> CFString?](./cmtimemappingcopydescription%28allocator,mapping%29.md)
  Copies a string description of a time mapping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimemappingshow(_:))*