# kCLLocationAccuracyReduced

**Framework**: Core Location  
**Kind**: var

The level of accuracy used when an app isn’t authorized for full accuracy location data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
let kCLLocationAccuracyReduced: CLLocationAccuracy
```

#### Discussion

The accuracy of location data is reduced in both space and time using approaches like selecting a nearby point of interest and updating the location at most a few times per hour. The approximate location preserves the user’s country or region, typically preserves the city, and is usually within 1–20 kilometers of the actual location.

If your app is authorized to access location information with full accuracy, you can use this constant to access location data as if the app didn’t have that authorization.

## See Also

- [let kCLLocationAccuracyBestForNavigation: CLLocationAccuracy](kcllocationaccuracybestfornavigation.md)
  The highest possible accuracy that uses additional sensor data to facilitate navigation apps.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/kcllocationaccuracyreduced)*