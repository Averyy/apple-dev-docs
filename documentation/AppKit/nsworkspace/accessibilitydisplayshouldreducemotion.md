# accessibilityDisplayShouldReduceMotion

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the accessibility option to reduce motion is in an enabled state.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var accessibilityDisplayShouldReduceMotion: Bool { get }
```

```objc
@property (readonly) BOOL accessibilityDisplayShouldReduceMotion;
```

## Discussion

If this property’s value is [`true`](../../Swift/true.md), avoid large animations, especially those that simulate the third dimension. To receive updates when this setting changes, register for the [`accessibilityDisplayOptionsDidChangeNotification`](./accessibilitydisplayoptionsdidchangenotification.md) notification using [`notificationCenter`](./notificationcenter.md).

## See Also

### Supporting Accessibility
- [var accessibilityDisplayShouldDifferentiateWithoutColor: Bool](./accessibilitydisplayshoulddifferentiatewithoutcolor.md)
  A Boolean value that indicates whether the app avoids conveying information through color alone.
- [var accessibilityDisplayShouldIncreaseContrast: Bool](./accessibilitydisplayshouldincreasecontrast.md)
  A Boolean value that indicates whether the app presents a high-contrast user interface.
- [var accessibilityDisplayShouldReduceTransparency: Bool](./accessibilitydisplayshouldreducetransparency.md)
  A Boolean value that indicates whether the app avoids using semitransparent backgrounds.
- [var accessibilityDisplayShouldInvertColors: Bool](./accessibilitydisplayshouldinvertcolors.md)
  A Boolean value that indicates whether the accessibility option to invert colors is in an enabled state.
- [var isSwitchControlEnabled: Bool](./isswitchcontrolenabled.md)
  A Boolean value that indicates whether Switch Control is currently running.
- [var isVoiceOverEnabled: Bool](./isvoiceoverenabled.md)
  A Boolean value that indicates whether VoiceOver is currently running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/accessibilitydisplayshouldreducemotion)*