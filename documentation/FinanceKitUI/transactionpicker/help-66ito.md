# help(_:)

**Framework**: FinanceKitUI  
**Kind**: method

Adds help text to a view using a localized string resource that you provide.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func help(_ textKey: LocalizedStringResource) -> some View
```

#### Discussion

Adding help to a view configures the view’s accessibility hint and its help tag (also called a ) in macOS or visionOS. For more information on using help tags, see [`Offering help`](https://developer.apple.com/design/Human-Interface-Guidelines/offering-help) in the Human Interface Guidelines.

```None
Button(action: composeMessage) {
    Image(systemName: "square.and.pencil")
}
.help("Compose a new message")
```

## Parameters

- `textKey`: Text resource for the localized text to use as help.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker/help(_:)-66ito)*