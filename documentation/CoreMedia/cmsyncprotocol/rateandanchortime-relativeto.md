# rateAndAnchorTime(relativeTo:)

**Framework**: Core Media  
**Kind**: method  
**Required**: Yes

Queries the relative rate of one timebase or clock relative to another timebase or clock, and the times of each timebase or clock at which the relative rate went into effect.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
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

- [func rate<T>(relativeTo: T) -> Double](cmsyncprotocol/rate(relativeto:).md)
  Queries the relative rate of one timebase or clock relative to another timebase or clock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsyncprotocol/rateandanchortime(relativeto:))*