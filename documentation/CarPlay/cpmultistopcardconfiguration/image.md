# image

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An optional image displayed alongside the @c title in the options panel, serving as an entry point to the multi-stop panel.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@NSCopying
var image: UIImage? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) UIImage * image;
```

## See Also

### Getting the configuration details
- [var title: String?](./title.md)
  Title of panel presented to configure waypoints along a route. If no panel is provided, the panel title will default to “Add Stop”.
- [var buttons: [CPTextButton]](./buttons.md)
  An array of text buttons to be displayed at the bottom of the card presented to configure waypoints along a route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmultistopcardconfiguration/image)*