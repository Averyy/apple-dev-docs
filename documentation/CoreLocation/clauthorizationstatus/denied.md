# CLAuthorizationStatus.denied

**Framework**: Core Location  
**Kind**: case  
**Role**: Case

The user denied the use of location services for the app or they are disabled globally in Settings.

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
case denied
```

```c
kCLAuthorizationStatusDenied
```

## Discussion

When the authorization status is denied, your app can’t use location services. The status can be denied when:

- The user denied location permissions for your app.
- The user turned off location services for the device in Settings.
- Location services are unavailable because the device is in Airplane mode.

If the user re-enables location services in Settings, your app’s authorization returns to its previous state. The status change is reported to your delegate’s [`locationManager(_:didChangeAuthorization:)`](../cllocationmanagerdelegate/locationmanager%28_,didchangeauthorization%29.md) method.

You may call [`locationServicesEnabled()`](../cllocationmanager/locationservicesenabled%28%29.md) if you wish to determine whether location services are available globally on the device.

## See Also

### Getting the authorization status
- [CLAuthorizationStatus.notDetermined](./notdetermined.md)
  The user has not chosen whether the app can use location services.
- [CLAuthorizationStatus.restricted](./restricted.md)
  The app is not authorized to use location services.
- [static var authorized: CLAuthorizationStatus](./authorized.md)
  The user authorized the app to use location services.
- [CLAuthorizationStatus.authorizedAlways](./authorizedalways.md)
  The user authorized the app to start location services at any time.
- [CLAuthorizationStatus.authorizedWhenInUse](./authorizedwheninuse.md)
  The user authorized the app to start location services while it is in use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/denied)*