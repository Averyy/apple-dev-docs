# sessionConfiguration(_:contentStyleChanged:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate about changes to the interface’s appearance.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func sessionConfiguration(_ sessionConfiguration: CPSessionConfiguration, contentStyleChanged contentStyle: CPContentStyle)
```

```objc
- (void) sessionConfiguration:(CPSessionConfiguration *) sessionConfiguration contentStyleChanged:(CPContentStyle) contentStyle;
```

## Discussion

Use this method to toggle your interface between a light or dark style. When the ambient light levels change, a vehicle might update this value to ensure content on the center display remains easy to see.

## Parameters

- `sessionConfiguration`: The session configuration object that reports the change.

## See Also

### Handling environmental changes
- [func sessionConfiguration(CPSessionConfiguration, limitedUserInterfacesChanged: CPLimitableUserInterface)](./sessionconfiguration%28_,limiteduserinterfaceschanged%29.md)
  Tells the delegate about changes to the availability of interface features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsessionconfigurationdelegate/sessionconfiguration(_:contentstylechanged:))*