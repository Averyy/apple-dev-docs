# CMTimeMakeWithSeconds(_:preferredTimescale:)

**Framework**: Core Media  
**Kind**: func

Creates a time that represents a number of seconds in a preferred timescale.

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
func CMTimeMakeWithSeconds(_ seconds: Float64, preferredTimescale: Int32) -> CMTime
```

#### Return Value

A time structure.

#### Discussion

Specify a positive preferred timescale value, or the resulting time is [`invalid`](cmtime/invalid.md).

If you specify a value that causes an overflow, the system repeatedly halves the value until the overflow goes away or the timescale equals `1`. If the value still overflows at that point, the system sets the value to positive or negative infinity.

Query the [`hasBeenRounded`](cmtimeflags/hasbeenrounded.md) property value to determine whether the value, when converted back to seconds, precisely matches the original seconds value.

## Parameters

- `seconds`: The number of seconds to represent.
- `preferredTimescale`: The preferred timescale of the time.

## See Also

- [func CMTimeMake(value: Int64, timescale: Int32) -> CMTime](cmtimemake(value:timescale:).md)
  Creates a time with a value and timescale.
- [func CMTimeMakeWithEpoch(value: Int64, timescale: Int32, epoch: Int64) -> CMTime](cmtimemakewithepoch(value:timescale:epoch:).md)
  Creates a time with a value, timescale, and epoch.
- [func CMTimeMakeFromDictionary(CFDictionary?) -> CMTime](cmtimemakefromdictionary(_:).md)
  Creates a time from a dictionary representation of its fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimemakewithseconds(_:preferredtimescale:))*