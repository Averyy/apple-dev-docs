# homeManager(_:didUpdate:)

**Framework**: HomeKit  
**Kind**: method

Tells the delegate when the authorization status changes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
optional func homeManager(_ manager: HMHomeManager, didUpdate status: HMHomeManagerAuthorizationStatus)
```

## Parameters

- `manager`: The home manager for which the status changed.
- `status`: The new authorization status. You can also read this value at any time from the manager’s   property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanagerdelegate/homemanager(_:didupdate:))*