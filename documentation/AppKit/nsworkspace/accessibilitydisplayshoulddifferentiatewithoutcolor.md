# accessibilityDisplayShouldDifferentiateWithoutColor

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the app avoids conveying information through color alone.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var accessibilityDisplayShouldDifferentiateWithoutColor: Bool { get }
```

#### Discussion

If this property is [`true`](https://developer.apple.com/documentation/Swift/true), the user interface avoids conveying information using color alone. Instead, use shapes or glyphs to convey important information.

Users can change this setting by choosing System Preferences > Accessibility > Display and selecting the “Differentiate without color” option. To receive updates when this setting changes, register for the [`accessibilityDisplayOptionsDidChangeNotification`](nsworkspace/accessibilitydisplayoptionsdidchangenotification.md) notification using [`notificationCenter`](nsworkspace/notificationcenter.md).

## See Also

- [var accessibilityDisplayShouldIncreaseContrast: Bool](nsworkspace/accessibilitydisplayshouldincreasecontrast.md)
  A Boolean value that indicates whether the app presents a high-contrast user interface.
- [var accessibilityDisplayShouldReduceTransparency: Bool](nsworkspace/accessibilitydisplayshouldreducetransparency.md)
  A Boolean value that indicates whether the app avoids using semitransparent backgrounds.
- [var accessibilityDisplayShouldInvertColors: Bool](nsworkspace/accessibilitydisplayshouldinvertcolors.md)
  A Boolean value that indicates whether the accessibility option to invert colors is in an enabled state.
- [var accessibilityDisplayShouldReduceMotion: Bool](nsworkspace/accessibilitydisplayshouldreducemotion.md)
  A Boolean value that indicates whether the accessibility option to reduce motion is in an enabled state.
- [var isSwitchControlEnabled: Bool](nsworkspace/isswitchcontrolenabled.md)
  A Boolean value that indicates whether Switch Control is currently running.
- [var isVoiceOverEnabled: Bool](nsworkspace/isvoiceoverenabled.md)
  A Boolean value that indicates whether VoiceOver is currently running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/accessibilitydisplayshoulddifferentiatewithoutcolor)*