# rate(relativeTo:)

**Framework**: Core Media  
**Kind**: method  
**Required**: Yes

Queries the relative rate of one timebase or clock relative to another timebase or clock.

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
func rate<T>(relativeTo clockOrTimebase: T) -> Double where T : CMSyncProtocol
```

## Parameters

- `clockOrTimebase`: The clock to compare to.

## See Also

- [func rateAndAnchorTime<T>(relativeTo: T) throws -> (rate: Double, anchorTime: CMTime, referenceTime: CMTime)](cmsyncprotocol/rateandanchortime(relativeto:).md)
  Queries the relative rate of one timebase or clock relative to another timebase or clock, and the times of each timebase or clock at which the relative rate went into effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsyncprotocol/rate(relativeto:))*