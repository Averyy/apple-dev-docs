# sessionConfiguration(_:limitedUserInterfacesChanged:)

**Framework**: CarPlay  
**Kind**: method

Tells the delegate that the system changed keyboard or list limits on the user interface.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func sessionConfiguration(_ sessionConfiguration: CPSessionConfiguration, limitedUserInterfacesChanged limitedUserInterfaces: CPLimitableUserInterface)
```

## Parameters

- `sessionConfiguration`: The current session configuration.
- `limitedUserInterfaces`: A bit mask value indicating the user interface limits that changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsessionconfigurationdelegate/sessionconfiguration(_:limiteduserinterfaceschanged:))*