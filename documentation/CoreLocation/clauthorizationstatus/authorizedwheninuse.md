# CLAuthorizationStatus.authorizedWhenInUse

**Framework**: Core Location  
**Kind**: case  
**Role**: Case

The user authorized the app to start location services while it is in use.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case authorizedWhenInUse
```

```c
kCLAuthorizationStatusAuthorizedWhenInUse
```

#### Discussion

This authorization allows you to use all location services and receive location events only when your app is in use. To continue using location services in the background, enable Continuous Background Location Updates and start the services while the app is in use.

## See Also

### Getting the authorization status
- [CLAuthorizationStatus.notDetermined](./notdetermined.md)
  The user has not chosen whether the app can use location services.
- [CLAuthorizationStatus.restricted](./restricted.md)
  The app is not authorized to use location services.
- [CLAuthorizationStatus.denied](./denied.md)
  The user denied the use of location services for the app or they are disabled globally in Settings.
- [static var authorized: CLAuthorizationStatus](./authorized.md)
  The user authorized the app to use location services.
- [CLAuthorizationStatus.authorizedAlways](./authorizedalways.md)
  The user authorized the app to start location services at any time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/authorizedwheninuse)*