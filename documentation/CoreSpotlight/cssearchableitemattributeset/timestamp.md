# timestamp

**Framework**: Core Spotlight  
**Kind**: property

The timestamp on the item.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var timestamp: Date? { get set }
```

#### Discussion

The value of this property is generally used to specify the time at which the event captured by the item took place.

## See Also

- [var altitude: NSNumber?](cssearchableitemattributeset/altitude.md)
  The altitude of the item in meters above sea level, expressed using the WGS84 datum.
- [var city: String?](cssearchableitemattributeset/city.md)
  The city of the item’s origin according to guidelines that the provider establishes.
- [var country: String?](cssearchableitemattributeset/country.md)
  The full, publishable name of the country or region in which the intellectual property of the item was created, according to guidelines the provider establishes.
- [var gpsAreaInformation: String?](cssearchableitemattributeset/gpsareainformation.md)
  Information about the GPS area.
- [var gpsdop: NSNumber?](cssearchableitemattributeset/gpsdop.md)
  The GPS dilution of precision value.
- [var gpsDateStamp: Date?](cssearchableitemattributeset/gpsdatestamp.md)
  The date and time related to the GPS value.
- [var gpsDestBearing: NSNumber?](cssearchableitemattributeset/gpsdestbearing.md)
  The bearing to the destination point.
- [var gpsDestDistance: NSNumber?](cssearchableitemattributeset/gpsdestdistance.md)
  The distance to the destination point.
- [var gpsDestLatitude: NSNumber?](cssearchableitemattributeset/gpsdestlatitude.md)
  The latitude of the destination point.
- [var gpsDestLongitude: NSNumber?](cssearchableitemattributeset/gpsdestlongitude.md)
  The longitude of the destination point.
- [var gpsDifferental: NSNumber?](cssearchableitemattributeset/gpsdifferental.md)
  The differential correction applied to the GPS receiver.
- [var gpsMapDatum: String?](cssearchableitemattributeset/gpsmapdatum.md)
  The geodetic data that the GPS receiver uses.
- [var gpsMeasureMode: String?](cssearchableitemattributeset/gpsmeasuremode.md)
  The measurement precision mode in use by the GPS receiver.
- [var gpsProcessingMethod: String?](cssearchableitemattributeset/gpsprocessingmethod.md)
  The location finding method that the GPS receiver uses.
- [var gpsStatus: String?](cssearchableitemattributeset/gpsstatus.md)
  The status of the GPS receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/timestamp)*