# epoch

**Framework**: Core Media  
**Kind**: property  
**Role**: Instance Property

The epoch of the time.

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
var epoch: CMTimeEpoch
```

```c
CMTimeEpoch epoch;
```

#### Discussion

Use the epoch to differentiate between equal timestamps that are different due to looping, multi-item sequencing, and so on.

## See Also

### Accessing Time Values
- [var value: CMTimeValue](./value.md)
  A time value that represents the numerator of a rational time.
- [var timescale: CMTimeScale](./timescale.md)
  A timescale that represents the denominator of a rational time.
- [var flags: CMTimeFlags](./flags.md)
  The flags associated with a time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtime/epoch)*