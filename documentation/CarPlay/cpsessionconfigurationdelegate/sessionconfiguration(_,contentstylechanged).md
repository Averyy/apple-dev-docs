# sessionConfiguration(_:contentStyleChanged:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the vehicle changed its selected content style.

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

#### Discussion

The vehicle selects the content style according to the ambient light level, which can change periodically. Use this method to make sure your navigation app is always drawing the most appropriate style of map content in its base view.

## Parameters

- `sessionConfiguration`: The current session configuration.
- `contentStyle`: The vehicle’s selected content style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpsessionconfigurationdelegate/sessionconfiguration(_:contentstylechanged:))*