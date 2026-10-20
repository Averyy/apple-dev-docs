# CMTimeMappingMakeEmpty(target:)

**Framework**: Core Media  
**Kind**: func

Creates a valid time mapping with an empty source.

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
func CMTimeMappingMakeEmpty(target: CMTimeRange) -> CMTimeMapping
```

#### Return Value

A new time mapping.

#### Discussion

The target time range must have a duration whose epoch is `0`, otherwise the system returns an invalid time mapping.

## Parameters

- `target`: A time range on the target timeline.

## See Also

- [func CMTimeMappingMake(source: CMTimeRange, target: CMTimeRange) -> CMTimeMapping](cmtimemappingmake(source:target:).md)
  Creates a time mapping with a source and target time range.
- [func CMTimeMappingMakeFromDictionary(CFDictionary) -> CMTimeMapping](cmtimemappingmakefromdictionary(_:).md)
  Creates a time mapping from a dictionary representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimemappingmakeempty(target:))*