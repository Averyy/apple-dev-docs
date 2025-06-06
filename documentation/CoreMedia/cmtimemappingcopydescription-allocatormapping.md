# CMTimeMappingCopyDescription(allocator:mapping:)

**Framework**: Core Media  
**Kind**: func

Copies a string description of a time mapping.

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
func CMTimeMappingCopyDescription(allocator: CFAllocator?, mapping: CMTimeMapping) -> CFString?
```

#### Return Value

A string description of a time mapping.

## Parameters

- `allocator`: An allocator to use to create a dictionary. Pass   to use the default allocator.
- `mapping`: The time mapping from which to copy a description.

## See Also

- [func CMTimeMappingCopyAsDictionary(CMTimeMapping, allocator: CFAllocator?) -> CFDictionary?](cmtimemappingcopyasdictionary(_:allocator:).md)
  Returns a dictionary representation of a time mapping.
- [func CMTimeMappingShow(CMTimeMapping)](cmtimemappingshow(_:).md)
  Prints a description of a time mapping to standard output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimemappingcopydescription(allocator:mapping:))*