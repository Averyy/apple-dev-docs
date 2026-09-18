# buttonConfiguration

**Framework**: CarPlay  
**Kind**: property

The button information and travel estimates to display in the panel.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
var buttonConfiguration: CPMapPanelButtonConfiguration? { get }
```

#### Discussion

You specify this information initially when you create the panel, but can also update it by assigning a new value to this property. The property stores the buttons and other map-related information to display in the panel.

The system pins the information in this type to the bottom of the map panel, keeping it visible at all times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanel/buttonconfiguration)*