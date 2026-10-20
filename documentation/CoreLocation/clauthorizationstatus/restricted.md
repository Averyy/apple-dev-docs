# CLAuthorizationStatus.restricted

**Framework**: Core Location  
**Kind**: case  
**Role**: Case

The app is not authorized to use location services.

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
case restricted
```

```c
kCLAuthorizationStatusRestricted
```

#### Discussion

The user cannot change this app’s status, possibly due to active restrictions such as parental controls being in place.

## See Also

### Getting the authorization status
- [CLAuthorizationStatus.notDetermined](./notdetermined.md)
  The user has not chosen whether the app can use location services.
- [CLAuthorizationStatus.denied](./denied.md)
  The user denied the use of location services for the app or they are disabled globally in Settings.
- [static var authorized: CLAuthorizationStatus](./authorized.md)
  The user authorized the app to use location services.
- [CLAuthorizationStatus.authorizedAlways](./authorizedalways.md)
  The user authorized the app to start location services at any time.
- [CLAuthorizationStatus.authorizedWhenInUse](./authorizedwheninuse.md)
  The user authorized the app to start location services while it is in use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/restricted)*