# rateAndAnchorTime(relativeTo:)

**Framework**: Core Media  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Queries the relative rate of one timebase or clock relative to another timebase or clock, and the times of each timebase or clock at which the relative rate went into effect.

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
func rateAndAnchorTime<T>(relativeTo clockOrTimebase: T) throws -> (rate: Double, anchorTime: CMTime, referenceTime: CMTime) where T : CMSyncProtocol
```

## Parameters

- `clockOrTimebase`: The clock to compare to.

## See Also

### Getting the Time Rate
- [func rate<T>(relativeTo: T) -> Double](./rate%28relativeto%29.md)
  Queries the relative rate of one timebase or clock relative to another timebase or clock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsyncprotocol/rateandanchortime(relativeto:))*