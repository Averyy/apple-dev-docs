# CPMapPanelButtonConfiguration

**Framework**: CarPlay  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
class CPMapPanelButtonConfiguration
```

## Topics

### Initializers
- [init(primaryAction: CPTextButton, symbolButton: CPButton?, travelEstimates: CPTravelEstimates?)](cpmappanelbuttonconfiguration/init(primaryaction:symbolbutton:travelestimates:).md)
  Initializes a map panel button configuration with a primary action, optional travel estimates, and an optional secondary button.
### Instance Properties
- [var symbolButton: CPButton?](cpmappanelbuttonconfiguration/symbolbutton.md)
  An optional secondary button shown with this configuration. Note: only the image property of this button is used.
- [var travelEstimates: CPTravelEstimates?](cpmappanelbuttonconfiguration/travelestimates.md)
  Optional travel estimates displayed alongside the primary action.

## Relationships

### Inherits From
- [CPPanelButtonConfiguration](cppanelbuttonconfiguration.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanelbuttonconfiguration)*