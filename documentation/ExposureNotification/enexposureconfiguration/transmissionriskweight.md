# transmissionRiskWeight

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Instance Property

The weight assigned to a score for the affected user’s estimated risk of transmission.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var transmissionRiskWeight: Double { get set }
```

```objc
@property (nonatomic, assign, readwrite) double transmissionRiskWeight;
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.5 and later.

This weight parameter is not used.

## See Also

### Weight Configuration
- [var attenuationWeight: Double](./attenuationweight.md)
  The weight assigned to a score for the Bluetooth signal strength.
- [var daysSinceLastExposureWeight: Double](./dayssincelastexposureweight.md)
  The weight assigned to a score for the days since the user’s exposure.
- [var durationWeight: Double](./durationweight.md)
  The weight assigned to a score for the duration of the user’s exposure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enexposureconfiguration/transmissionriskweight)*