# flags

**Framework**: Core Video  
**Kind**: property  
**Role**: Instance Property

The flags associated with the `CVTime` value. See [CVTime Values](../cvtime-values.md) for possible values. If `kCVTimeIsIndefinite` is set, you should not use any of the other fields in this structure.

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
var flags: Int32
```

```c
int32_t flags;
```

## See Also

### Properties
- [var timeScale: Int32](./timescale.md)
  The time scale for this value.
- [var timeValue: Int64](./timevalue.md)
  The time value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvtime/flags)*