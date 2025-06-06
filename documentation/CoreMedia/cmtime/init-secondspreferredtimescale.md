# init(seconds:preferredTimescale:)

**Framework**: Core Media  
**Kind**: init

Creates a time that represents number of seconds in a preferred timescale.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst ?+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(seconds: Double, preferredTimescale: CMTimeScale)
```

#### Discussion

Specify a positive preferred timescale value, or the resulting time is [`invalid`](cmtime/invalid.md).

If you specify a value that causes an overflow, the system repeatedly halves the value until the overflow goes away or the timescale equals `1`. If the value still overflows at that point, the system sets the value to positive or negative infinity.

Query the [`hasBeenRounded`](cmtimeflags/hasbeenrounded.md) property value to determine whether the value, when converted back to seconds, precisely matches the original seconds value.

## Parameters

- `seconds`: The number of seconds to represent.
- `preferredTimescale`: The preferred timescale of the time.

## See Also

- [init(value: CMTimeValue, timescale: CMTimeScale)](cmtime/init(value:timescale:).md)
  Creates a time with a value and timescale.
- [init(value: CMTimeValue, timescale: CMTimeScale, flags: CMTimeFlags, epoch: CMTimeEpoch)](cmtime/init(value:timescale:flags:epoch:).md)
  Creates a time with a value, timescale, flags, and epoch.
- [init()](cmtime/init.md)
  Creates a time with an invalid value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtime/init(seconds:preferredtimescale:))*