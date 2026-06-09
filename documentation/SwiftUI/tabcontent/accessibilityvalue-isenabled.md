# accessibilityValue(_:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method

Adds a textual description of the value that the tab contains.

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
func accessibilityValue(_ valueDescription: Text, isEnabled: Bool = true) -> some TabContent<Self.TabValue>
```

#### Discussion

Use this method to describe the value represented by a tab, but only if that’s different than the tab’s label such as when an icon represent information about a tab.

```swift
var body: some View {
    TabView {
        Tab {
            MessagesView()
        } label: {
            Text("Messages")
        }
        .badge(30)
        .accessibilityValue("30 Unread")
    }
}
```

## Parameters

- `valueDescription`: The accessibility value to apply.
- `isEnabled`: If true the accessibility value is applied; otherwise the accessibility value is unchanged.

## See Also

- [func accessibilityHint(_:isEnabled:)](tabcontent/accessibilityhint(_:isenabled:).md)
  Communicates to the user what happens after selecting the tab.
- [func accessibilityIdentifier(String, isEnabled: Bool) -> some TabContent<Self.TabValue>
](tabcontent/accessibilityidentifier(_:isenabled:).md)
  Uses the string you specify to identify the view. Use this value for testing. It isn’t visible to the user.
- [func accessibilityInputLabels(_:isEnabled:)](tabcontent/accessibilityinputlabels(_:isenabled:).md)
  Sets alternate input labels with which users identify a tab.
- [func accessibilityLabel(_:isEnabled:)](tabcontent/accessibilitylabel(_:isenabled:).md)
  Adds a label to the tab that describes its contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/accessibilityvalue(_:isenabled:))*