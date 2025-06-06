# startTime

**Framework**: Model I/O  
**Kind**: property

The timestamp for the first timed data sample in the asset.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var startTime: TimeInterval { get set }
```

#### Discussion

Timed data in an asset is clamped to the start and end times—requesting sample data for a time sample before the start time returns the sample data at the start time.

If the asset does not contain timed information, this property’s value is zero.

## See Also

- [var frameInterval: TimeInterval](mdlasset/frameinterval.md)
  The time interval between data samples in the asset.
- [var endTime: TimeInterval](mdlasset/endtime.md)
  The timestamp for the last timed data sample in the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlasset/starttime)*