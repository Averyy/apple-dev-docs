# symbolOnly

**Framework**: CarPlay  
**Kind**: property  
**Role**: Type Property

Only the symbol appears for the maneuver.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
static var symbolOnly: CPManeuverDisplayStyle { get }
```

```c
CPManeuverDisplayStyleSymbolOnly
```

## Discussion

If your app provides lane guidance, include a second maneuver to the navigation session’s [`upcomingManeuvers`](../cpnavigationsession/upcomingmaneuvers.md) array that provides the lane guidance information. The second maneuver should have:

- A [`symbolSet`](../cpmaneuver/symbolset.md) containing dark and light images that fill the full width of the guidance panel with a maximum image size of 120 pt x 18 pt.
- An empty array of [`instructionVariants`](../cpmaneuver/instructionvariants.md).

The map template should include a [`mapDelegate`](../cpmaptemplate/mapdelegate.md) object that conforms to [`CPMapTemplateDelegate`](../cpmaptemplatedelegate.md) and implements the [`mapTemplate(_:displayStyleFor:)`](../cpmaptemplatedelegate/maptemplate%28_,displaystylefor%29.md) method, which returns the [`symbolOnly`](./symbolonly.md) display style for the maneuver.

## See Also

### Display Styles
- [static var leadingSymbol: CPManeuverDisplayStyle](./leadingsymbol.md)
  The symbol appears before the instructions for the maneuver.
- [static var trailingSymbol: CPManeuverDisplayStyle](./trailingsymbol.md)
  The symbol appears after the instructions for the maneuver.
- [static var instructionOnly: CPManeuverDisplayStyle](./instructiononly.md)
  Only the instructions appear for the maneuver.
- [CPManeuverDisplayStyleDefault](./cpmaneuverdisplaystyledefault.md)
  The default display style for the maneuver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaneuverdisplaystyle/symbolonly)*