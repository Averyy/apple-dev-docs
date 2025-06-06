# locationManager(_:didVisit:)

**Framework**: Core Location  
**Kind**: method

Tells the delegate that a new visit-related event was received.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
optional func locationManager(_ manager: CLLocationManager, didVisit visit: CLVisit)
```

#### Discussion

The location manager calls this method whenever it has new visit event to report to your app.

## Parameters

- `manager`: The location manager object reporting the event.
- `visit`: The visit object that contains the information about the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/locationmanager(_:didvisit:))*