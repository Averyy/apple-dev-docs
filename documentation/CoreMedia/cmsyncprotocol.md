# CMSyncProtocol

**Framework**: Core Media  
**Kind**: protocol  
**Role**: Protocol

A type that provides behavior for syncing time.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
protocol CMSyncProtocol : Sendable
```

## Topics

### Getting the Time
- [var time: CMTime](./cmsyncprotocol/time.md)
  The current time.
### Converting Time
- [func convertTime<T>(CMTime, to: T) -> CMTime](./cmsyncprotocol/converttime%28_,to%29.md)
  Converts a time from one timebase or clock to another timebase or clock.
### Getting the Time Rate
- [func rate<T>(relativeTo: T) -> Double](./cmsyncprotocol/rate%28relativeto%29.md)
  Queries the relative rate of one timebase or clock relative to another timebase or clock.
- [func rateAndAnchorTime<T>(relativeTo: T) throws -> (rate: Double, anchorTime: CMTime, referenceTime: CMTime)](./cmsyncprotocol/rateandanchortime%28relativeto%29.md)
  Queries the relative rate of one timebase or clock relative to another timebase or clock, and the times of each timebase or clock at which the relative rate went into effect.
### Determining Time Drift
- [func mightDrift<T>(relativeTo: T) -> Bool](./cmsyncprotocol/mightdrift%28relativeto%29.md)
  Returns a Boolean value that indicates whether it’s possible for the clock to drift relative to the input.

## Relationships

### Inherits From
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Conforming Types
- [CMClock](./cmclock.md)
- [CMTimebase](./cmtimebase.md)

## See Also

### Data Types
- [class CMTimebase](./cmtimebase.md)
  A model of a timeline under application control.
- [struct CMSync](./cmsync.md)
  A type that represents time syncing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsyncprotocol)*