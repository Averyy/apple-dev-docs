# CPMultiStopCardConfiguration

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
class CPMultiStopCardConfiguration
```

```objc
@interface CPMultiStopCardConfiguration : NSObject
```

## Topics

### Initializers
- [init?(coder: NSCoder)](./cpmultistopcardconfiguration/init%28coder%29.md)
- [init(title: String?, buttons: [CPTextButton])](./cpmultistopcardconfiguration/init%28title,buttons%29.md)
  Initializes a MultiStopCardConfiguration with an optional title and an array of text buttons
- [init(title: String?, buttons: [CPTextButton], image: UIImage?)](./cpmultistopcardconfiguration/init%28title,buttons,image%29.md)
  Initializes a MultiStopCardConfiguration with an optional title, an array of text buttons, and an optional image
### Instance Properties
- [var buttons: [CPTextButton]](./cpmultistopcardconfiguration/buttons.md)
  An array of text buttons to be displayed at the bottom of the card presented to configure waypoints along a route.
- [var image: UIImage?](./cpmultistopcardconfiguration/image.md)
  An optional image displayed alongside the @c title in the options panel, serving as an entry point to the multi-stop panel.
- [var title: String?](./cpmultistopcardconfiguration/title.md)
  Title of panel presented to configure waypoints along a route. If no panel is provided, the panel title will default to “Add Stop”.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmultistopcardconfiguration)*