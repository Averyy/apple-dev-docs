# accessibilityDisplayShouldDifferentiateWithoutColor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the app avoids conveying information through color alone.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var accessibilityDisplayShouldDifferentiateWithoutColor: Bool { get }
```

```objc
@property (readonly) BOOL accessibilityDisplayShouldDifferentiateWithoutColor;
```

#### Discussion

If this property is [`true`](../../Swift/true.md), the user interface avoids conveying information using color alone. Instead, use shapes or glyphs to convey important information.

Users can change this setting by choosing System Preferences > Accessibility > Display and selecting the “Differentiate without color” option. To receive updates when this setting changes, register for the [`accessibilityDisplayOptionsDidChangeNotification`](./accessibilitydisplayoptionsdidchangenotification.md) notification using [`notificationCenter`](./notificationcenter.md).

## See Also

### Supporting Accessibility
- [var accessibilityDisplayShouldIncreaseContrast: Bool](./accessibilitydisplayshouldincreasecontrast.md)
  A Boolean value that indicates whether the app presents a high-contrast user interface.
- [var accessibilityDisplayShouldReduceTransparency: Bool](./accessibilitydisplayshouldreducetransparency.md)
  A Boolean value that indicates whether the app avoids using semitransparent backgrounds.
- [var accessibilityDisplayShouldInvertColors: Bool](./accessibilitydisplayshouldinvertcolors.md)
  A Boolean value that indicates whether the accessibility option to invert colors is in an enabled state.
- [var accessibilityDisplayShouldReduceMotion: Bool](./accessibilitydisplayshouldreducemotion.md)
  A Boolean value that indicates whether the accessibility option to reduce motion is in an enabled state.
- [var isSwitchControlEnabled: Bool](./isswitchcontrolenabled.md)
  A Boolean value that indicates whether Switch Control is currently running.
- [var isVoiceOverEnabled: Bool](./isvoiceoverenabled.md)
  A Boolean value that indicates whether VoiceOver is currently running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/accessibilitydisplayshoulddifferentiatewithoutcolor)*