# CMTimeMappingMakeFromDictionary(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a time mapping from a dictionary representation.

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
func CMTimeMappingMakeFromDictionary(_ dictionaryRepresentation: CFDictionary) -> CMTimeMapping
```

```c
extern CMTimeMapping CMTimeMappingMakeFromDictionary(CFDictionaryRef dictionaryRepresentation);
```

## Return Value

A new time mapping.

## Discussion

If the dictionary you provide doesn’t have the requisite keyed values, the system returns an invalid time mapping.

## Parameters

- `dictionaryRepresentation`: A dictionary representation of a time mapping that you previously created by calling the [`CMTimeMappingCopyAsDictionary(_:allocator:)`](./cmtimemappingcopyasdictionary%28_,allocator%29.md) function.

## See Also

### Creating Time Mappings
- [func CMTimeMappingMake(source: CMTimeRange, target: CMTimeRange) -> CMTimeMapping](./cmtimemappingmake%28source,target%29.md)
  Creates a time mapping with a source and target time range.
- [func CMTimeMappingMakeEmpty(target: CMTimeRange) -> CMTimeMapping](./cmtimemappingmakeempty%28target%29.md)
  Creates a valid time mapping with an empty source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimemappingmakefromdictionary(_:))*