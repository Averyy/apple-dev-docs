# mapTemplate(_:displayStyleFor:)

**Framework**: CarPlay  
**Kind**: method

Asks the delegate for the maneuver’s display style.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, displayStyleFor maneuver: CPManeuver) -> CPManeuverDisplayStyle
```

#### Return Value

A display style that determines the visual layout for the maneuver.

#### Discussion

The display style only applies to the second maneuver that you provide in the navigation session’s [`upcomingManeuvers`](cpnavigationsession/upcomingmaneuvers.md) array.

## Parameters

- `mapTemplate`: The current map template.
- `maneuver`: The maneuver that the system applies the display style to.

## See Also

- [struct CPManeuverDisplayStyle](cpmaneuverdisplaystyle.md)
  A display style that determines the visual layout for a maneuver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:displaystylefor:))*