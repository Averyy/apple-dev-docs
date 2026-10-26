# CPManeuverDisplayStyle

**Framework**: CarPlay  
**Kind**: struct  
**Role**: Structure

A display style that determines the visual layout for a maneuver.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
struct CPManeuverDisplayStyle
```

```c
enum CPManeuverDisplayStyle : NSInteger;
```

## Topics

### Display Styles
- [static var leadingSymbol: CPManeuverDisplayStyle](./cpmaneuverdisplaystyle/leadingsymbol.md)
  The symbol appears before the instructions for the maneuver.
- [static var trailingSymbol: CPManeuverDisplayStyle](./cpmaneuverdisplaystyle/trailingsymbol.md)
  The symbol appears after the instructions for the maneuver.
- [static var instructionOnly: CPManeuverDisplayStyle](./cpmaneuverdisplaystyle/instructiononly.md)
  Only the instructions appear for the maneuver.
- [static var symbolOnly: CPManeuverDisplayStyle](./cpmaneuverdisplaystyle/symbolonly.md)
  Only the symbol appears for the maneuver.
- [CPManeuverDisplayStyleDefault](./cpmaneuverdisplaystyle/cpmaneuverdisplaystyledefault.md)
  The default display style for the maneuver.
### Initializers
- [init(rawValue: Int)](./cpmaneuverdisplaystyle/init%28rawvalue%29.md)
  Initializes a maneuver display style using the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Setting the Display Style
- [func mapTemplate(CPMapTemplate, displayStyleFor: CPManeuver) -> CPManeuverDisplayStyle](./cpmaptemplatedelegate/maptemplate%28_,displaystylefor%29.md)
  Asks the delegate for the maneuver’s display style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaneuverdisplaystyle)*