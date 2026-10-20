# locationManager(_:didChangeAuthorization:)

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Tells the delegate its authorization status when the app creates the location manager and when the authorization status changes.

**Availability**:
- iOS 4.2+ - Deprecated in 14.0
- iPadOS 4.2+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.7+ - Deprecated in 11.0
- tvOS 9.0+ - Deprecated in 14.0
- watchOS 1.0+ - Deprecated in 7.0

> **Deprecated**: Use [`locationManagerDidChangeAuthorization(_:)`](./locationmanagerdidchangeauthorization%28_%29.md) instead.

## Declaration

```swift
optional func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus)
```

```objc
- (void) locationManager:(CLLocationManager *) manager didChangeAuthorizationStatus:(CLAuthorizationStatus) status;
```

## Parameters

- `manager`: The location manager object reporting the event.
- `status`: The authorization status for the app.

## See Also

### Responding to authorization changes
- [func locationManagerDidChangeAuthorization(CLLocationManager)](./locationmanagerdidchangeauthorization%28_%29.md)
  Tells the delegate when the app creates the location manager and when the authorization status changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didchangeauthorization:))*