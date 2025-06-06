# init()

**Framework**: Core Media  
**Kind**: init

Creates a time with an invalid value.

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
init()
```

#### Discussion

Using this initializer creates a time equal to [`invalid`](cmtime/invalid.md).

## See Also

- [init(value: CMTimeValue, timescale: CMTimeScale)](cmtime/init(value:timescale:).md)
  Creates a time with a value and timescale.
- [init(value: CMTimeValue, timescale: CMTimeScale, flags: CMTimeFlags, epoch: CMTimeEpoch)](cmtime/init(value:timescale:flags:epoch:).md)
  Creates a time with a value, timescale, flags, and epoch.
- [init(seconds: Double, preferredTimescale: CMTimeScale)](cmtime/init(seconds:preferredtimescale:).md)
  Creates a time that represents number of seconds in a preferred timescale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtime/init())*