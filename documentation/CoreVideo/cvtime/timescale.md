# timeScale

**Framework**: Core Video  
**Kind**: property  
**Role**: Instance Property

The time scale for this value.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var timeScale: Int32
```

```c
int32_t timeScale;
```

## See Also

### Properties
- [var flags: Int32](./flags.md)
  The flags associated with the `CVTime` value. See [CVTime Values](../cvtime-values.md) for possible values. If `kCVTimeIsIndefinite` is set, you should not use any of the other fields in this structure.
- [var timeValue: Int64](./timevalue.md)
  The time value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvtime/timescale)*