# kCLErrorUserInfoAlternateRegionKey

**Framework**: Core Location  
**Kind**: var

A key in the user information dictionary of an error relating to a delayed region-monitoring response.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
let kCLErrorUserInfoAlternateRegionKey: String
```

#### Discussion

This key is included in an error of type [`regionMonitoringResponseDelayed`](clerror-swift.struct/regionmonitoringresponsedelayed.md). The value is a [`CLRegion`](clregion.md) object containing the region that location services can monitor more effectively.

## See Also

- [struct CLError](clerror-swift.struct.md)
  A Core Location error.
- [let kCLErrorDomain: String](kclerrordomain.md)
  The domain for Core Location errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/kclerroruserinfoalternateregionkey)*