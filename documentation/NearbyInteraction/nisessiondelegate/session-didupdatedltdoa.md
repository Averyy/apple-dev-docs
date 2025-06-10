# session(_:didUpdateDLTDOA:)

**Framework**: Nearby Interaction  
**Kind**: method

This is called when new updates about DL-TDOA measurement are available.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
optional func session(_ session: NISession, didUpdateDLTDOA measurements: [NIDLTDOAMeasurement])
```

#### Discussion

> **Note**: This will only be called after successfully running an NISession with an NIDLTDOAConfiguration.

## Parameters

- `session`: The session that updated NI DL-TDOA measurement.
- `measurements`: The measurements update from a NI DL-TDOA session


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisessiondelegate/session(_:didupdatedltdoa:))*