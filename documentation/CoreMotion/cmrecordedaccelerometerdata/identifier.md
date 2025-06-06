# identifier

**Framework**: Core Motion  
**Kind**: property

The unique identifier for the accelerometer data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var identifier: UInt64 { get }
```

#### Discussion

Accelerometer data is recorded in batches, which are assigned a unique identifier. This property contains the identifier of the batch in which this particular sample was recorded.

## See Also

- [var startDate: Date](cmrecordedaccelerometerdata/startdate.md)
  The wall clock time when the sensor sample was recorded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata/identifier)*