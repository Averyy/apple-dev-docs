# help(_:)

**Framework**: App Intents  
**Kind**: method

Adds help text to a view using a localized string that you provide.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func help(_ textKey: LocalizedStringKey) -> some View
```

#### Discussion

Adding help to a view configures the view’s accessibility hint and its help tag (also called a ) in macOS or visionOS. For more information on using help tags, see [`Offering help`](https://developer.apple.com/design/Human-Interface-Guidelines/offering-help) in the Human Interface Guidelines.

```swift
Button(action: composeMessage) {
    Image(systemName: "square.and.pencil")
}
.help("Compose a new message")
```

## Parameters

- `textKey`: The key for the localized text to use as help.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/help(_:)-3m9wt)*