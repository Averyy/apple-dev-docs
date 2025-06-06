# CMTimeMappingCopyAsDictionary(_:allocator:)

**Framework**: Core Media  
**Kind**: func

Returns a dictionary representation of a time mapping.

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
func CMTimeMappingCopyAsDictionary(_ mapping: CMTimeMapping, allocator: CFAllocator?) -> CFDictionary?
```

#### Return Value

A dictionary representation of a time mapping.

## Parameters

- `mapping`: The time mapping for which to create a dictionary representation.
- `allocator`: An allocator to use to create a dictionary. Pass   to use the default allocator.

## See Also

- [func CMTimeMappingCopyDescription(allocator: CFAllocator?, mapping: CMTimeMapping) -> CFString?](cmtimemappingcopydescription(allocator:mapping:).md)
  Copies a string description of a time mapping.
- [func CMTimeMappingShow(CMTimeMapping)](cmtimemappingshow(_:).md)
  Prints a description of a time mapping to standard output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimemappingcopyasdictionary(_:allocator:))*