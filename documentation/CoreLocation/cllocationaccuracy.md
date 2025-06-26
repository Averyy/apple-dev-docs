# CLLocationAccuracy

**Framework**: Core Location  
**Kind**: typealias

The accuracy of a geographical coordinate.

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
typealias CLLocationAccuracy = Double
```

#### Discussion

When reported in a [`CLLocation`](cllocation.md) object, accuracy values are the number of meters from the original geographic coordinate that could yield the user’s actual location. When specifying values for the [`desiredAccuracy`](cllocationmanager/desiredaccuracy.md) property of your [`CLLocationManager`](cllocationmanager.md) object, use one of the appropriate constants.

## Topics

### Desired Accuracy Constants
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
- [let kCLLocationAccuracyReduced: CLLocationAccuracy](kcllocationaccuracyreduced.md)
  The level of accuracy used when an app isn’t authorized for full accuracy location data.

## See Also

- [var horizontalAccuracy: CLLocationAccuracy](cllocation/horizontalaccuracy.md)
  The radius of uncertainty for the location, measured in meters.
- [var verticalAccuracy: CLLocationAccuracy](cllocation/verticalaccuracy.md)
  The validity of the altitude values, and their estimated uncertainty, measured in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationaccuracy)*