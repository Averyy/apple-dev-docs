# isVoiceOverEnabled

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether VoiceOver is currently running.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var isVoiceOverEnabled: Bool { get }
```

```objc
@property (readonly, getter=isVoiceOverEnabled) BOOL voiceOverEnabled;
```

#### Discussion

You can observe this property with key-value observing.

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
- [var accessibilityDisplayShouldReduceMotion: Bool](./accessibilitydisplayshouldreducemotion.md)
  A Boolean value that indicates whether the accessibility option to reduce motion is in an enabled state.
- [var isSwitchControlEnabled: Bool](./isswitchcontrolenabled.md)
  A Boolean value that indicates whether Switch Control is currently running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/isvoiceoverenabled)*