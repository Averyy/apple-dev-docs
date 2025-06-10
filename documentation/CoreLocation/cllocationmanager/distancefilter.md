# distanceFilter

**Framework**: Core Location  
**Kind**: property

The minimum distance in meters the device must move horizontally before an update event is generated.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var distanceFilter: CLLocationDistance { get set }
```

## Mentions

- [Getting the current location of a device](getting-the-current-location-of-a-device.md)

#### Discussion

This location manager measures this relative to the previously delivered location. Specify the value `kCLDistanceFilterNone` to receive notifications for all movements. The default value of this property is `kCLDistanceFilterNone`.

Use this property only in conjunction with the Standard location services and not with the Significant-change or Visits services.

##### Special Considerations

In iOS, this property is declared as `nonatomic`. In macOS, it is declared as `atomic`.

## See Also

- [var desiredAccuracy: CLLocationAccuracy](cllocationmanager/desiredaccuracy.md)
  The accuracy of the location data that your app wants to receive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/distancefilter)*