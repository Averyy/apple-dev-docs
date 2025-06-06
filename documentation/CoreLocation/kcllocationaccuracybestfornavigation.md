# kCLLocationAccuracyBestForNavigation

**Framework**: Core Location  
**Kind**: var

The highest possible accuracy that uses additional sensor data to facilitate navigation apps.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCLLocationAccuracyBestForNavigation: CLLocationAccuracy
```

#### Discussion

This level of accuracy is intended for use in navigation apps that require precise position information at all times. Because of the extra power requirements, use this level of accuracy only while the device is plugged in.

This level of accurate is available only if `isAuthorizedForPreciseLocation` is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [let kCLLocationAccuracyBest: CLLocationAccuracy](kcllocationaccuracybest.md)
  The best level of accuracy available.
- [let kCLLocationAccuracyNearestTenMeters: CLLocationAccuracy](kcllocationaccuracynearesttenmeters.md)
  Accurate to within ten meters of the desired target.
- [let kCLLocationAccuracyHundredMeters: CLLocationAccuracy](kcllocationaccuracyhundredmeters.md)
  Accurate to within one hundred meters.
- [let kCLLocationAccuracyKilometer: CLLocationAccuracy](kcllocationaccuracykilometer.md)
  Accurate to the nearest kilometer.
- [let kCLLocationAccuracyThreeKilometers: CLLocationAccuracy](kcllocationaccuracythreekilometers.md)
  Accurate to the nearest three kilometers.
- [let kCLLocationAccuracyReduced: CLLocationAccuracy](kcllocationaccuracyreduced.md)
  The level of accuracy used when an app isn’t authorized for full accuracy location data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/kcllocationaccuracybestfornavigation)*