# CPMultiStopCardConfiguration

**Framework**: CarPlay  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
class CPMultiStopCardConfiguration
```

## Topics

### Initializers
- [init?(coder: NSCoder)](cpmultistopcardconfiguration/init(coder:).md)
- [init(title: String?, buttons: [CPTextButton])](cpmultistopcardconfiguration/init(title:buttons:).md)
  Initializes a MultiStopCardConfiguration with an optional title and an array of text buttons
### Instance Properties
- [var buttons: [CPTextButton]](cpmultistopcardconfiguration/buttons.md)
  An array of text buttons to be displayed at the bottom of the card presented to configure waypoints along a route.
- [var title: String?](cpmultistopcardconfiguration/title.md)
  Title of card presented to configure waypoints along a route. If no title is provided, the card title will default to “Trip Overview”.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmultistopcardconfiguration)*