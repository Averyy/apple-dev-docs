# CPManeuverDisplayStyle

**Framework**: CarPlay  
**Kind**: struct

A display style that determines the visual layout for a maneuver.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
struct CPManeuverDisplayStyle
```

## Topics

### Display Styles
- [static var leadingSymbol: CPManeuverDisplayStyle](cpmaneuverdisplaystyle/leadingsymbol.md)
  The symbol appears before the instructions for the maneuver.
- [static var trailingSymbol: CPManeuverDisplayStyle](cpmaneuverdisplaystyle/trailingsymbol.md)
  The symbol appears after the instructions for the maneuver.
- [static var instructionOnly: CPManeuverDisplayStyle](cpmaneuverdisplaystyle/instructiononly.md)
  Only the instructions appear for the maneuver.
- [static var symbolOnly: CPManeuverDisplayStyle](cpmaneuverdisplaystyle/symbolonly.md)
  Only the symbol appears for the maneuver.
### Initializers
- [init(rawValue: Int)](cpmaneuverdisplaystyle/init(rawvalue:).md)
  Initializes a maneuver display style using the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func mapTemplate(CPMapTemplate, displayStyleFor: CPManeuver) -> CPManeuverDisplayStyle](cpmaptemplatedelegate/maptemplate(_:displaystylefor:).md)
  Asks the delegate for the maneuver’s display style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaneuverdisplaystyle)*