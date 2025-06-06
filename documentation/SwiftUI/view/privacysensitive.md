# privacySensitive(_:)

**Framework**: SwiftUI  
**Kind**: method

Marks the view as containing sensitive, private user data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func privacySensitive(_ sensitive: Bool = true) -> some View
```

#### Discussion

SwiftUI redacts views marked with this modifier when you apply the [`privacy`](redactionreasons/privacy.md) redaction reason.

```swift
struct BankAccountView: View {
    var body: some View {
        VStack {
            Text("Account #")

            Text(accountNumber)
                .font(.headline)
                .privacySensitive() // Hide only the account number.
        }
    }
}
```

## See Also

- [Designing your app for the Always On state](../watchOS-Apps/designing-your-app-for-the-always-on-state.md)
  Customize your watchOS app’s user interface for continuous display.
- [func redacted(reason: RedactionReasons) -> some View](view/redacted(reason:).md)
  Adds a reason to apply a redaction to this view hierarchy.
- [func unredacted() -> some View](view/unredacted.md)
  Removes any reason to apply a redaction to this view hierarchy.
- [var redactionReasons: RedactionReasons](environmentvalues/redactionreasons.md)
  The current redaction reasons applied to the view hierarchy.
- [var isSceneCaptured: Bool](environmentvalues/isscenecaptured.md)
  The current capture state.
- [struct RedactionReasons](redactionreasons.md)
  The reasons to apply a redaction to data displayed on screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/privacysensitive(_:))*