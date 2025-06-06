# CLAuthorizationStatus.notDetermined

**Framework**: Core Location  
**Kind**: case

The user has not chosen whether the app can use location services.

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
case notDetermined
```

## Mentions

- [Requesting authorization to use location services](requesting-authorization-to-use-location-services.md)

#### Discussion

When the authorization status is Not Determined, request authorization causes the location manager to prompt the user for permission if the app is in the foreground. See [`requestWhenInUseAuthorization()`](cllocationmanager/requestwheninuseauthorization().md) and [`requestAlwaysAuthorization()`](cllocationmanager/requestalwaysauthorization().md) for more information.

## See Also

- [CLAuthorizationStatus.restricted](clauthorizationstatus/restricted.md)
  The app is not authorized to use location services.
- [CLAuthorizationStatus.denied](clauthorizationstatus/denied.md)
  The user denied the use of location services for the app or they are disabled globally in Settings.
- [static var authorized: CLAuthorizationStatus](clauthorizationstatus/authorized.md)
  The user authorized the app to use location services.
- [CLAuthorizationStatus.authorizedAlways](clauthorizationstatus/authorizedalways.md)
  The user authorized the app to start location services at any time.
- [CLAuthorizationStatus.authorizedWhenInUse](clauthorizationstatus/authorizedwheninuse.md)
  The user authorized the app to start location services while it is in use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/notdetermined)*