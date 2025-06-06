# menuIndicator(_:)

**Framework**: Journaling Suggestions  
**Kind**: method

Sets the menu indicator visibility for controls within this view.

**Availability**:
- iOS 15.0+
- macOS 12.0+
- tvOS 17.0+

## Declaration

```swift
nonisolated
func menuIndicator(_ visibility: Visibility) -> some View
```

#### Discussion

Use this modifier to override the default menu indicator visibility for controls in this view. For example, the code below creates a menu without an indicator:

```None
Menu {
    ForEach(history , id: \.self) { historyItem in
        Button(historyItem.title) {
            self.openURL(historyItem.url)
        }
    }
} label: {
    Label("Back", systemImage: "chevron.backward")
        .labelStyle(.iconOnly)
} primaryAction: {
    if let last = history.last {
        self.openURL(last.url)
    }
}
.menuIndicator(.hidden)
```

> **Note**: On tvOS, the standard button styles do not include a menu indicator, so this modifier will have no effect when using a built-in button style. You can implement an indicator in your own `ButtonStyle` implementation by checking the value of the `menuIndicatorVisibility` environment value.

On tvOS, the standard button styles do not include a menu indicator, so this modifier will have no effect when using a built-in button style. You can implement an indicator in your own `ButtonStyle` implementation by checking the value of the `menuIndicatorVisibility` environment value.

## Parameters

- `visibility`: The menu indicator visibility to apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/menuindicator(_:))*