# buttons

**Framework**: CarPlay  
**Kind**: property

An array of text buttons to be displayed at the bottom of the card presented to configure waypoints along a route.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
var buttons: [CPTextButton] { get }
```

#### Discussion

> **Note**: The multi-stop card may display a maximum of 2 buttons. Setting more than 2 buttons to this property will only display the first 2 buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmultistopcardconfiguration/buttons)*