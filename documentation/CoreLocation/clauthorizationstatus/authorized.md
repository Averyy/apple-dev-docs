# authorized

**Framework**: Core Location  
**Kind**: property  
**Role**: Type Property

The user authorized the app to use location services.

**Availability**:
- iOS 2.0+ - Deprecated in 8.0
- iPadOS 2.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.6+

> **Deprecated**: For iOS, use [`CLAuthorizationStatus.authorizedAlways`](./authorizedalways.md) or [`CLAuthorizationStatus.authorizedWhenInUse`](./authorizedwheninuse.md) instead.

## Declaration

```swift
static var authorized: CLAuthorizationStatus { get }
```

```c
kCLAuthorizationStatusAuthorized
```

## See Also

### Getting the authorization status
- [CLAuthorizationStatus.notDetermined](./notdetermined.md)
  The user has not chosen whether the app can use location services.
- [CLAuthorizationStatus.restricted](./restricted.md)
  The app is not authorized to use location services.
- [CLAuthorizationStatus.denied](./denied.md)
  The user denied the use of location services for the app or they are disabled globally in Settings.
- [CLAuthorizationStatus.authorizedAlways](./authorizedalways.md)
  The user authorized the app to start location services at any time.
- [CLAuthorizationStatus.authorizedWhenInUse](./authorizedwheninuse.md)
  The user authorized the app to start location services while it is in use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/authorized)*