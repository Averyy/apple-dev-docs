# CMTimeMakeFromDictionary(_:)

**Framework**: Core Media  
**Kind**: func

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

#### Return Value

A time structure.

#### Discussion

For keys in the dictionary, see [`Dictionary Keys`](cmtime-dictionary-keys.md).

## Parameters

- `dictionaryRepresentation`: A dictionary created from a call to  .

## See Also

- [func CMTimeMake(value: Int64, timescale: Int32) -> CMTime](cmtimemake(value:timescale:).md)
  Creates a time with a value and timescale.
- [func CMTimeMakeWithEpoch(value: Int64, timescale: Int32, epoch: Int64) -> CMTime](cmtimemakewithepoch(value:timescale:epoch:).md)
  Creates a time with a value, timescale, and epoch.
- [func CMTimeMakeWithSeconds(Float64, preferredTimescale: Int32) -> CMTime](cmtimemakewithseconds(_:preferredtimescale:).md)
  Creates a time that represents a number of seconds in a preferred timescale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimemakefromdictionary(_:))*