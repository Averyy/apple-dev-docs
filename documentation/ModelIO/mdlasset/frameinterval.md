# frameInterval

**Framework**: Model I/O  
**Kind**: property

The time interval between data samples in the asset.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var frameInterval: TimeInterval { get set }
```

#### Discussion

If the asset does not contain timed information, this property’s value is zero. Otherwise, this property represents frame timing: For example, if an asset contains animation data to be presented at 24 frames per second, this property’s value is `0.04167` (1/24 second).

## See Also

- [var startTime: TimeInterval](mdlasset/starttime.md)
  The timestamp for the first timed data sample in the asset.
- [var endTime: TimeInterval](mdlasset/endtime.md)
  The timestamp for the last timed data sample in the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlasset/frameinterval)*