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
- `isEnabled`: If true the accessibility hint is applied; otherwise the accessibility hint is unchanged.

## See Also

- [func accessibilityIdentifier(String, isEnabled: Bool) -> some TabContent<Self.TabValue>
](tabcontent/accessibilityidentifier(_:isenabled:).md)
  Uses the string you specify to identify the view. Use this value for testing. It isn’t visible to the user.
- [func accessibilityInputLabels(_:isEnabled:)](tabcontent/accessibilityinputlabels(_:isenabled:).md)
  Sets alternate input labels with which users identify a tab.
- [func accessibilityLabel(_:isEnabled:)](tabcontent/accessibilitylabel(_:isenabled:).md)
  Adds a label to the tab that describes its contents.
- [func accessibilityValue(_:isEnabled:)](tabcontent/accessibilityvalue(_:isenabled:).md)
  Adds a textual description of the value that the tab contains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/accessibilityhint(_:isenabled:))*