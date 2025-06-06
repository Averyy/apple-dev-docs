# init(value:timescale:flags:epoch:)

**Framework**: Core Media  
**Kind**: init

Creates a time with a value, timescale, flags, and epoch.

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
init(value: CMTimeValue, timescale: CMTimeScale, flags: CMTimeFlags, epoch: CMTimeEpoch)
```

## Parameters

- `value`: An integer time value.
- `timescale`: An integer timescale value.
- `flags`: Optional flags to specify for the time.
- `epoch`: An epoch for the time, which is typically  .

## See Also

- [init(value: CMTimeValue, timescale: CMTimeScale)](cmtime/init(value:timescale:).md)
  Creates a time with a value and timescale.
- [init(seconds: Double, preferredTimescale: CMTimeScale)](cmtime/init(seconds:preferredtimescale:).md)
  Creates a time that represents number of seconds in a preferred timescale.
- [init()](cmtime/init.md)
  Creates a time with an invalid value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtime/init(value:timescale:flags:epoch:))*