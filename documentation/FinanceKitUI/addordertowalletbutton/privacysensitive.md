# privacySensitive(_:)

**Framework**: FinanceKitUI  
**Kind**: method

Marks the view as containing sensitive, private user data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
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

```None
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/addordertowalletbutton/privacysensitive(_:))*