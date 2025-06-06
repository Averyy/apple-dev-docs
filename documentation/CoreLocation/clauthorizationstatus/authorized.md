# authorized

**Framework**: Core Location  
**Kind**: property

The user authorized the app to use location services.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+

## Declaration

```swift
static var authorized: CLAuthorizationStatus { get }
```

## See Also

- [CLAuthorizationStatus.notDetermined](clauthorizationstatus/notdetermined.md)
  The user has not chosen whether the app can use location services.
- [CLAuthorizationStatus.restricted](clauthorizationstatus/restricted.md)
  The app is not authorized to use location services.
- [CLAuthorizationStatus.denied](clauthorizationstatus/denied.md)
  The user denied the use of location services for the app or they are disabled globally in Settings.
- [CLAuthorizationStatus.authorizedAlways](clauthorizationstatus/authorizedalways.md)
  The user authorized the app to start location services at any time.
- [CLAuthorizationStatus.authorizedWhenInUse](clauthorizationstatus/authorizedwheninuse.md)
  The user authorized the app to start location services while it is in use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/authorized)*