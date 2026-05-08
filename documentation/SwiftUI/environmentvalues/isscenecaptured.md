# isSceneCaptured

**Framework**: SwiftUI  
**Kind**: property

The current capture state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
var isSceneCaptured: Bool { get set }
```

#### Discussion

Use this value to determine whether the scene is actively being cloned to another destination (like during AirPlay) or is being mirrored or recorded.

Your app can respond to changes in this value to take appropriate action, like obscuring content.

## See Also

- [Designing your app for the Always On state](../watchOS-Apps/designing-your-app-for-the-always-on-state.md)
  Customize your watchOS app’s user interface for continuous display.
- [Protecting sensitive content when screen sharing and remote control are active](protecting-sensitive-content-when-screen-sharing.md)
  Detect active screen capture sessions and respond appropriately to protect sensitive content in your app.
- [func privacySensitive(Bool) -> some View](view/privacysensitive(_:).md)
  Marks the view as containing sensitive, private user data.
- [func redacted(reason: RedactionReasons) -> some View](view/redacted(reason:).md)
  Adds a reason to apply a redaction to this view hierarchy.
- [func unredacted() -> some View](view/unredacted.md)
  Removes any reason to apply a redaction to this view hierarchy.
- [var redactionReasons: RedactionReasons](environmentvalues/redactionreasons.md)
  The current redaction reasons applied to the view hierarchy.
- [struct RedactionReasons](redactionreasons.md)
  The reasons to apply a redaction to data displayed on screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/isscenecaptured)*