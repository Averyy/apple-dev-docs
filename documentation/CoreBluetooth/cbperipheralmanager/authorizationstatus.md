# authorizationStatus()

**Framework**: Core Bluetooth  
**Kind**: method

Returns the app’s authorization status for sharing data while in the background.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func authorizationStatus() -> CBPeripheralManagerAuthorizationStatus
```

#### Return Value

A value that indicates whether the app has authorization to share data using Bluetooth services while in the background. For a list of possible values, see [`CBPeripheralManagerAuthorizationStatus`](cbperipheralmanagerauthorizationstatus.md).

#### Discussion

The system manages the authorization status of a given app, and considers several factors. The user must explicitly authorize apps to share data using Bluetooth services while in the background state. The system automatically displays a request for user authorization when your app first attempts to use Bluetooth services to share data.

Calling this method doesn’t prompt the user for access. Instead, you use this method to detect restricted access and hide any affected UI features from the user.

## See Also

- [enum CBPeripheralManagerAuthorizationStatus](cbperipheralmanagerauthorizationstatus.md)
  Values representing the current authorization state of the peripheral manager.
- [enum CBPeripheralManagerState](cbperipheralmanagerstate.md)
  Values that represent the current state of the peripheral manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbperipheralmanager/authorizationstatus())*