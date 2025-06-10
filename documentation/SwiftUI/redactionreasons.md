# RedactionReasons

**Framework**: SwiftUI  
**Kind**: struct

The reasons to apply a redaction to data displayed on screen.

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
struct RedactionReasons
```

## Topics

### Getting redaction reasons
- [static let invalidated: RedactionReasons](redactionreasons/invalidated.md)
  Displayed data should appear as invalidated and pending a new update.
- [static let placeholder: RedactionReasons](redactionreasons/placeholder.md)
  Displayed data should appear as generic placeholders.
- [static let privacy: RedactionReasons](redactionreasons/privacy.md)
  Displayed data should be obscured to protect private information.
### Creating redaction reasons
- [init(rawValue: Int)](redactionreasons/init(rawvalue:).md)
  Creates a new set from a raw value.
- [let rawValue: Int](redactionreasons/rawvalue.md)
  The raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Designing your app for the Always On state](../watchOS-Apps/designing-your-app-for-the-always-on-state.md)
  Customize your watchOS app’s user interface for continuous display.
- [func privacySensitive(Bool) -> some View](view/privacysensitive(_:).md)
  Marks the view as containing sensitive, private user data.
- [func redacted(reason: RedactionReasons) -> some View](view/redacted(reason:).md)
  Adds a reason to apply a redaction to this view hierarchy.
- [func unredacted() -> some View](view/unredacted.md)
  Removes any reason to apply a redaction to this view hierarchy.
- [var redactionReasons: RedactionReasons](environmentvalues/redactionreasons.md)
  The current redaction reasons applied to the view hierarchy.
- [var isSceneCaptured: Bool](environmentvalues/isscenecaptured.md)
  The current capture state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/redactionreasons)*