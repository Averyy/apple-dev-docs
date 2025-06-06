# windowDuration

**Framework**: Sound Analysis  
**Kind**: property

The duration of the audio buffer the request sends to the underlying sound classifier for each prediction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var windowDuration: CMTime { get set }
```

#### Discussion

Configure the window duration with a value that satisfies the request’s [`windowDurationConstraint`](snclassifysoundrequest/windowdurationconstraint-5no60.md).

The request sends larger audio buffer windows less frequently, which can make the classifications more accurate, but less precise in indicating when they occur. Requests with smaller buffer window durations sharpen the time resolution of each prediction, but send smaller audio buffers to the sound classifier.

## See Also

- [var overlapFactor: Double](snclassifysoundrequest/overlapfactor.md)
  The amount of overlap between successive analysis windows when the model operates on a fixed-size audio block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snclassifysoundrequest/windowduration)*