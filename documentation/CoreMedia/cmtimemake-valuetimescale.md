# CMTimeMake(value:timescale:)

**Framework**: Core Media  
**Kind**: func

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

#### Return Value

A time structure.

## Parameters

- `value`: An integer time value.
- `timescale`: An integer timescale.

## See Also

- [func CMTimeMakeWithEpoch(value: Int64, timescale: Int32, epoch: Int64) -> CMTime](cmtimemakewithepoch(value:timescale:epoch:).md)
  Creates a time with a value, timescale, and epoch.
- [func CMTimeMakeWithSeconds(Float64, preferredTimescale: Int32) -> CMTime](cmtimemakewithseconds(_:preferredtimescale:).md)
  Creates a time that represents a number of seconds in a preferred timescale.
- [func CMTimeMakeFromDictionary(CFDictionary?) -> CMTime](cmtimemakefromdictionary(_:).md)
  Creates a time from a dictionary representation of its fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimemake(value:timescale:))*