# timeValue

**Framework**: Core Video  
**Kind**: property  
**Role**: Instance Property

The time value.

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
var timeValue: Int64
```

```c
int64_t timeValue;
```

## See Also

### Properties
- [var flags: Int32](./flags.md)
  The flags associated with the `CVTime` value. See [CVTime Values](../cvtime-values.md) for possible values. If `kCVTimeIsIndefinite` is set, you should not use any of the other fields in this structure.
- [var timeScale: Int32](./timescale.md)
  The time scale for this value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvtime/timevalue)*