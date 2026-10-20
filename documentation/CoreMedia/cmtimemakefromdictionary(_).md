# CMTimeMakeFromDictionary(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a time from a dictionary representation of its fields.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMTimeMakeFromDictionary(_ dictionaryRepresentation: CFDictionary?) -> CMTime
```

```c
extern CMTime CMTimeMakeFromDictionary(CFDictionaryRef dictionaryRepresentation);
```

#### Return Value

A time structure.

#### Discussion

For keys in the dictionary, see [Dictionary Keys](./cmtime-dictionary-keys.md).

## Parameters

- `dictionaryRepresentation`: A dictionary created from a call to [`CMTimeCopyAsDictionary(_:allocator:)`](./cmtimecopyasdictionary%28_,allocator%29.md).

## See Also

### Creating a Time
- [func CMTimeMake(value: Int64, timescale: Int32) -> CMTime](./cmtimemake%28value,timescale%29.md)
  Creates a time with a value and timescale.
- [func CMTimeMakeWithEpoch(value: Int64, timescale: Int32, epoch: Int64) -> CMTime](./cmtimemakewithepoch%28value,timescale,epoch%29.md)
  Creates a time with a value, timescale, and epoch.
- [func CMTimeMakeWithSeconds(Float64, preferredTimescale: Int32) -> CMTime](./cmtimemakewithseconds%28_,preferredtimescale%29.md)
  Creates a time that represents a number of seconds in a preferred timescale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimemakefromdictionary(_:))*