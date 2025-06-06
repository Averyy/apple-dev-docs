# CMTimeMappingMake(source:target:)

**Framework**: Core Media  
**Kind**: func

Creates a time mapping with a source and target time range.

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
func CMTimeMappingMake(source: CMTimeRange, target: CMTimeRange) -> CMTimeMapping
```

#### Return Value

A new time mapping.

#### Discussion

The source and target parameters must have durations whose epoch is `0`, otherwise the system returns an invalid time mapping.

## Parameters

- `source`: A time range on the source timeline.
- `target`: A time range on the target timeline.

## See Also

- [func CMTimeMappingMakeEmpty(target: CMTimeRange) -> CMTimeMapping](cmtimemappingmakeempty(target:).md)
  Creates a valid time mapping with an empty source.
- [func CMTimeMappingMakeFromDictionary(CFDictionary) -> CMTimeMapping](cmtimemappingmakefromdictionary(_:).md)
  Creates a time mapping from a dictionary representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimemappingmake(source:target:))*