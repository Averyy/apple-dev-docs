# redactionReasons

**Framework**: SwiftUI  
**Kind**: property

The current redaction reasons applied to the view hierarchy.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var redactionReasons: RedactionReasons { get set }
```

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
- [var isSceneCaptured: Bool](environmentvalues/isscenecaptured.md)
  The current capture state.
- [struct RedactionReasons](redactionreasons.md)
  The reasons to apply a redaction to data displayed on screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/redactionreasons)*