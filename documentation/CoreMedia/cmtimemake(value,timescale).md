# CMTimeMake(value:timescale:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a time with a value and timescale.

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
func CMTimeMake(value: Int64, timescale: Int32) -> CMTime
```

```c
extern CMTime CMTimeMake(int64_t value, int32_t timescale);
```

#### Return Value

A time structure.

## Parameters

- `value`: An integer time value.
- `timescale`: An integer timescale.

## See Also

### Creating a Time
- [func CMTimeMakeWithEpoch(value: Int64, timescale: Int32, epoch: Int64) -> CMTime](./cmtimemakewithepoch%28value,timescale,epoch%29.md)
  Creates a time with a value, timescale, and epoch.
- [func CMTimeMakeWithSeconds(Float64, preferredTimescale: Int32) -> CMTime](./cmtimemakewithseconds%28_,preferredtimescale%29.md)
  Creates a time that represents a number of seconds in a preferred timescale.
- [func CMTimeMakeFromDictionary(CFDictionary?) -> CMTime](./cmtimemakefromdictionary%28_%29.md)
  Creates a time from a dictionary representation of its fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimemake(value:timescale:))*