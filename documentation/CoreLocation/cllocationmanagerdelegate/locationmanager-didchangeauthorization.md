# locationManager(_:didChangeAuthorization:)

**Framework**: Core Location  
**Kind**: method

Tells the delegate its authorization status when the app creates the location manager and when the authorization status changes.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- watchOS 1.0+

## Declaration

```swift
optional func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus)
```

## Parameters

- `manager`: The location manager object reporting the event.
- `status`: The authorization status for the app.

## See Also

- [func locationManagerDidChangeAuthorization(CLLocationManager)](cllocationmanagerdelegate/locationmanagerdidchangeauthorization(_:).md)
  Tells the delegate when the app creates the location manager and when the authorization status changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didchangeauthorization:))*