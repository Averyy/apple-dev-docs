# gpsTrack

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

The direction of travel of the item in degrees from true north.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var gpsTrack: NSNumber? { get set }
```

```objc
@property (strong, nullable) NSNumber * GPSTrack;
```

## See Also

### Describing places
- [var altitude: NSNumber?](./altitude.md)
  The altitude of the item in meters above sea level, expressed using the WGS84 datum.
- [var city: String?](./city.md)
  The city of the item’s origin according to guidelines that the provider establishes.
- [var country: String?](./country.md)
  The full, publishable name of the country or region in which the intellectual property of the item was created, according to guidelines the provider establishes.
- [var gpsAreaInformation: String?](./gpsareainformation.md)
  Information about the GPS area.
- [var gpsdop: NSNumber?](./gpsdop.md)
  The GPS dilution of precision value.
- [var gpsDateStamp: Date?](./gpsdatestamp.md)
  The date and time related to the GPS value.
- [var gpsDestBearing: NSNumber?](./gpsdestbearing.md)
  The bearing to the destination point.
- [var gpsDestDistance: NSNumber?](./gpsdestdistance.md)
  The distance to the destination point.
- [var gpsDestLatitude: NSNumber?](./gpsdestlatitude.md)
  The latitude of the destination point.
- [var gpsDestLongitude: NSNumber?](./gpsdestlongitude.md)
  The longitude of the destination point.
- [var gpsDifferental: NSNumber?](./gpsdifferental.md)
  The differential correction applied to the GPS receiver.
- [var gpsMapDatum: String?](./gpsmapdatum.md)
  The geodetic data that the GPS receiver uses.
- [var gpsMeasureMode: String?](./gpsmeasuremode.md)
  The measurement precision mode in use by the GPS receiver.
- [var gpsProcessingMethod: String?](./gpsprocessingmethod.md)
  The location finding method that the GPS receiver uses.
- [var gpsStatus: String?](./gpsstatus.md)
  The status of the GPS receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/gpstrack)*