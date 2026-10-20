# CLAuthorizationStatus.authorizedAlways

**Framework**: Core Location  
**Kind**: case  
**Role**: Case

The user authorized the app to start location services at any time.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 9.0+
- watchOS 2.0+

## Declaration

```swift
case authorizedAlways
```

```c
kCLAuthorizationStatusAuthorizedAlways
```

#### Discussion

This authorization allows you to use all location services and receive location events whether or not your app is in use.

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
- [CLAuthorizationStatus.authorizedWhenInUse](./authorizedwheninuse.md)
  The user authorized the app to start location services while it is in use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/authorizedalways)*