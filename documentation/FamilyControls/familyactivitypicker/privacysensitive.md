# privacySensitive(_:)

**Framework**: FamilyControls  
**Kind**: method

Marks the view as containing sensitive, private user data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func privacySensitive(_ sensitive: Bool = true) -> some View
```

#### Discussion

SwiftUI redacts views marked with this modifier when you apply the `RedactionReasons/privacy` redaction reason.

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

- [func redacted(reason: RedactionReasons) -> some View](familyactivitypicker/redacted(reason:).md)
  Adds a reason to apply a redaction to this view hierarchy.
- [func unredacted() -> some View](familyactivitypicker/unredacted.md)
  Removes any reason to apply a redaction to this view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/privacysensitive(_:))*