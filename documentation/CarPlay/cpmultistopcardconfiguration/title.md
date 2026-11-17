# title

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

Title of panel presented to configure waypoints along a route. If no panel is provided, the panel title will default to “Add Stop”.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
var title: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * title;
```

## See Also

### Getting the configuration details
- [var image: UIImage?](./image.md)
  An optional image displayed alongside the @c title in the options panel, serving as an entry point to the multi-stop panel.
- [var buttons: [CPTextButton]](./buttons.md)
  An array of text buttons to be displayed at the bottom of the card presented to configure waypoints along a route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmultistopcardconfiguration/title)*