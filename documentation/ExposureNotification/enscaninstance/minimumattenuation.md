# minimumAttenuation

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Instance Property

The minimum attenuation of beacons received during the scan.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var minimumAttenuation: ENAttenuation { get }
```

```objc
@property (nonatomic, assign, readonly) ENAttenuation minimumAttenuation;
```

#### Discussion

> ❗ **Important**:  This property is available in iOS 12.5, and in iOS 13.7 and later.

## See Also

### Getting Scan Instance Properties
- [var secondsSinceLastScan: Int](./secondssincelastscan.md)
  The number of seconds elapsed since the previous scan.
- [var typicalAttenuation: ENAttenuation](./typicalattenuation.md)
  The aggregation of the attenuations of beacons received during the scan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enscaninstance/minimumattenuation)*