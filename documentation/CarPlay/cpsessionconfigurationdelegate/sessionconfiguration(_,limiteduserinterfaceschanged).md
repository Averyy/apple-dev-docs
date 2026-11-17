# sessionConfiguration(_:limitedUserInterfacesChanged:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate about changes to the availability of interface features.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func sessionConfiguration(_ sessionConfiguration: CPSessionConfiguration, limitedUserInterfacesChanged limitedUserInterfaces: CPLimitableUserInterface)
```

```objc
- (void) sessionConfiguration:(CPSessionConfiguration *) sessionConfiguration limitedUserInterfacesChanged:(CPLimitableUserInterface) limitedUserInterfaces;
```

## Discussion

The following example shows how to determine if keyboard interfaces are supported.

**Swift**:

```swift
func sessionConfiguration(_ sessionConfiguration: CPSessionConfiguration,
                                           limitedUserInterfacesChanged limitedUserInterfaces: CPLimitableUserInterface) {
    let hasKeyboard = limitedUserInterfaces.contains(.keyboard)
    // Do something with the value.
}
```

**Objective-C**:

```objc
- (void)sessionConfiguration:(CPSessionConfiguration *)sessionConfiguration limitedUserInterfacesChanged:(CPLimitableUserInterface)limitedUserInterfaces {
    Boolean hasKeyboard = limitedUserInterfaces & CPLimitableUserInterfaceKeyboard;
    // Do something with the value.
}
```

## Parameters

- `sessionConfiguration`: The session configuration object that reports the change.
- `limitedUserInterfaces`: The new set of limited user interfaces. Use this value to determine which features to enable or disable in your app. For example, if this value contains the [`keyboard`](../cplimitableuserinterface/keyboard.md) value, don’t display any templates that show a virtual keyboard.

## See Also

### Handling environmental changes
- [func sessionConfiguration(CPSessionConfiguration, contentStyleChanged: CPContentStyle)](./sessionconfiguration%28_,contentstylechanged%29.md)
  Tells the delegate about changes to the interface’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsessionconfigurationdelegate/sessionconfiguration(_:limiteduserinterfaceschanged:))*