# buttons

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An array of text buttons to be displayed at the bottom of the card presented to configure waypoints along a route.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
var buttons: [CPTextButton] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<CPTextButton *> * buttons;
```

## Discussion

> **Note**: The multi-stop card may display a maximum of 2 buttons. Setting more than 2 buttons to this property will only display the first 2 buttons.

## See Also

### Getting the configuration details
- [var title: String?](./title.md)
  Title of panel presented to configure waypoints along a route. If no panel is provided, the panel title will default to “Add Stop”.
- [var image: UIImage?](./image.md)
  An optional image displayed alongside the @c title in the options panel, serving as an entry point to the multi-stop panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmultistopcardconfiguration/buttons)*