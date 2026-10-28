# CBManagerAuthorization.restricted

**Framework**: Core Bluetooth  
**Kind**: case  
**Role**: Case

A state that indicates this app isn’t authorized to use Bluetooth.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case restricted
```

```c
CBManagerAuthorizationRestricted
```

## Discussion

In this state, the user can’t change the Bluetooth authorization status, possibly due to active restrictions such as parental controls.

## See Also

### Authorization States
- [CBManagerAuthorization.allowedAlways](./allowedalways.md)
  A state that indicates the user has authorized Bluetooth at any time.
- [CBManagerAuthorization.denied](./denied.md)
  A state that indicates the user explicitly denied Bluetooth access for this app.
- [CBManagerAuthorization.notDetermined](./notdetermined.md)
  A state that indicates the user has yet to authorize Bluetooth for this app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corebluetooth/cbmanagerauthorization/restricted)*