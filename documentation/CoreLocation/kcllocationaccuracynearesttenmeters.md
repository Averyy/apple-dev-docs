# kCLLocationAccuracyNearestTenMeters

**Framework**: Core Location  
**Kind**: var

Accurate to within ten meters of the desired target.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCLLocationAccuracyNearestTenMeters: CLLocationAccuracy
```

#### Discussion

This level of accurate is available only if `isAuthorizedForPreciseLocation` is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [let kCLLocationAccuracyBestForNavigation: CLLocationAccuracy](kcllocationaccuracybestfornavigation.md)
  The highest possible accuracy that uses additional sensor data to facilitate navigation apps.
- [let kCLLocationAccuracyBest: CLLocationAccuracy](kcllocationaccuracybest.md)
  The best level of accuracy available.
- [let kCLLocationAccuracyHundredMeters: CLLocationAccuracy](kcllocationaccuracyhundredmeters.md)
  Accurate to within one hundred meters.
- [let kCLLocationAccuracyKilometer: CLLocationAccuracy](kcllocationaccuracykilometer.md)
  Accurate to the nearest kilometer.
- [let kCLLocationAccuracyThreeKilometers: CLLocationAccuracy](kcllocationaccuracythreekilometers.md)
  Accurate to the nearest three kilometers.
- [let kCLLocationAccuracyReduced: CLLocationAccuracy](kcllocationaccuracyreduced.md)
  The level of accuracy used when an app isn’t authorized for full accuracy location data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/kcllocationaccuracynearesttenmeters)*