# transmissionRiskWeight

**Framework**: Exposure Notification  
**Kind**: property

The weight assigned to a score for the affected user’s estimated risk of transmission.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
var transmissionRiskWeight: Double { get set }
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.5 and later.

 This property is available in iOS 12.5, and in iOS 13.5 and later.

This weight parameter is not used.

## See Also

- [var attenuationWeight: Double](enexposureconfiguration/attenuationweight.md)
  The weight assigned to a score for the Bluetooth signal strength.
- [var daysSinceLastExposureWeight: Double](enexposureconfiguration/dayssincelastexposureweight.md)
  The weight assigned to a score for the days since the user’s exposure.
- [var durationWeight: Double](enexposureconfiguration/durationweight.md)
  The weight assigned to a score for the duration of the user’s exposure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposureconfiguration/transmissionriskweight)*