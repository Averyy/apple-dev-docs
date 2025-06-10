# accessibilityHint(_:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method

Communicates to the user what happens after selecting the tab.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func accessibilityHint(_ hint: LocalizedStringResource, isEnabled: Bool = true) -> some TabContent<Self.TabValue>
```

#### Discussion

Provide a hint in the form of a brief phrase, like “Open shopping cart” or “Show downloaded attachments”.

```swift
var body: some View {
    TabView {
        Tab {
            MessagesView()
        } label: {
            Image(systemName: "play")
        }
        .accessibilityHint("Select videos to download")
    }
}
```

## Parameters

- `hint`: The accessibility hint to apply.
- `isEnabled`: If true the accessibility hint is applied; otherwise the   accessibility hint is unchanged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/accessibilityhint(_:isenabled:))*