# accessibilityDisplayShouldReduceTransparency

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the app avoids using semitransparent backgrounds.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var accessibilityDisplayShouldReduceTransparency: Bool { get }
```

#### Discussion

If this property is [`true`](https://developer.apple.com/documentation/Swift/true), don’t use semitransparent backgrounds in the user interface. For example, use only opaque windows.

Users can change this setting by choosing System Preferences > Accessibility > Display and selecting the “Reduce transparency” option. To receive updates when this setting changes, register to the [`accessibilityDisplayOptionsDidChangeNotification`](nsworkspace/accessibilitydisplayoptionsdidchangenotification.md) notification using [`notificationCenter`](nsworkspace/notificationcenter.md).

## See Also

- [var accessibilityDisplayShouldDifferentiateWithoutColor: Bool](nsworkspace/accessibilitydisplayshoulddifferentiatewithoutcolor.md)
  A Boolean value that indicates whether the app avoids conveying information through color alone.
- [var accessibilityDisplayShouldIncreaseContrast: Bool](nsworkspace/accessibilitydisplayshouldincreasecontrast.md)
  A Boolean value that indicates whether the app presents a high-contrast user interface.
- [var accessibilityDisplayShouldInvertColors: Bool](nsworkspace/accessibilitydisplayshouldinvertcolors.md)
  A Boolean value that indicates whether the accessibility option to invert colors is in an enabled state.
- [var accessibilityDisplayShouldReduceMotion: Bool](nsworkspace/accessibilitydisplayshouldreducemotion.md)
  A Boolean value that indicates whether the accessibility option to reduce motion is in an enabled state.
- [var isSwitchControlEnabled: Bool](nsworkspace/isswitchcontrolenabled.md)
  A Boolean value that indicates whether Switch Control is currently running.
- [var isVoiceOverEnabled: Bool](nsworkspace/isvoiceoverenabled.md)
  A Boolean value that indicates whether VoiceOver is currently running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/accessibilitydisplayshouldreducetransparency)*