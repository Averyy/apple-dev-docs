# accessibilityPrefersCrossFadeTransitions

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the Reduce Motion and the Prefer Cross-Fade Transitions settings are in an enabled state.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
var accessibilityPrefersCrossFadeTransitions: Bool { get set }
```

## Discussion

If this property’s value is true, UI should avoid Slide animations and prefer Cross-Fade transitions instead

On macOS, this value returns solely whether the Reduce Motion setting is in an enabled state. On watchOS, this value always returns false.

## See Also

### Accessibility
- [var accessibilityAssistiveAccessEnabled: Bool](./accessibilityassistiveaccessenabled.md)
  A Boolean value that indicates whether Assistive Access is in use.
- [var accessibilityDimFlashingLights: Bool](./accessibilitydimflashinglights.md)
  Whether the setting to reduce flashing or strobing lights in video content is on. This setting can also be used to determine if UI in playback controls should be shown to indicate upcoming content that includes flashing or strobing lights.
- [var accessibilityDifferentiateWithoutColor: Bool](./accessibilitydifferentiatewithoutcolor.md)
  Whether the system preference for Differentiate without Color is enabled.
- [var accessibilityEnabled: Bool](./accessibilityenabled.md)
  A Boolean value that indicates whether the user has enabled an assistive technology.
- [var accessibilityInvertColors: Bool](./accessibilityinvertcolors.md)
  Whether the system preference for Invert Colors is enabled.
- [var accessibilityLargeContentViewerEnabled: Bool](./accessibilitylargecontentviewerenabled.md)
  Whether the Large Content Viewer is enabled.
- [var accessibilityPlayAnimatedImages: Bool](./accessibilityplayanimatedimages.md)
  Whether the setting for playing animations in an animated image is on. When this value is false, any presented image that contains animation should not play automatically.
- [var accessibilityPrefersHeadAnchorAlternative: Bool](./accessibilityprefersheadanchoralternative.md)
  Whether the system setting to prefer alternatives to head-anchored content is on.
- [var accessibilityQuickActionsEnabled: Bool](./accessibilityquickactionsenabled.md)
  A Boolean that indicates whether the quick actions feature is enabled.
- [var accessibilityReduceMotion: Bool](./accessibilityreducemotion.md)
  Whether the system preference for Reduce Motion is enabled.
- [var accessibilityReduceTransparency: Bool](./accessibilityreducetransparency.md)
  Whether the system preference for Reduce Transparency is enabled.
- [var accessibilitySwitchControlEnabled: Bool](./accessibilityswitchcontrolenabled.md)
  A Boolean value that indicates whether the Switch Control motor accessibility feature is in use.
- [var accessibilityVoiceOverEnabled: Bool](./accessibilityvoiceoverenabled.md)
  A Boolean value that indicates whether the VoiceOver screen reader is in use.
- [var legibilityWeight: LegibilityWeight?](./legibilityweight.md)
  The font weight to apply to text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilitypreferscrossfadetransitions)*