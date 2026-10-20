# CMTimeMappingCopyAsDictionary(_:allocator:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

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

```c
extern CFDictionaryRefCMTimeMappingCopyAsDictionary(CMTimeMapping mapping, CFAllocatorRef allocator);
```

#### Return Value

A dictionary representation of a time mapping.

## Parameters

- `mapping`: The time mapping for which to create a dictionary representation.
- `allocator`: An allocator to use to create a dictionary. Pass `kCFAllocatorDefault` to use the default allocator.

## See Also

### Representing Time Mappings
- [func CMTimeMappingCopyDescription(allocator: CFAllocator?, mapping: CMTimeMapping) -> CFString?](./cmtimemappingcopydescription%28allocator,mapping%29.md)
  Copies a string description of a time mapping.
- [func CMTimeMappingShow(CMTimeMapping)](./cmtimemappingshow%28_%29.md)
  Prints a description of a time mapping to standard output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimemappingcopyasdictionary(_:allocator:))*