# accessibilityInputLabels(_:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets alternate input labels with which users identify a tab.

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
func accessibilityInputLabels(_ inputLabelKeys: [LocalizedStringKey], isEnabled: Bool = true) -> some TabContent<Self.TabValue>
```

**Other overloads**:

```swift
nonisolated
func accessibilityInputLabels(_ inputLabels: [Text], isEnabled: Bool = true) -> some TabContent<Self.TabValue>
```

```swift
nonisolated
func accessibilityInputLabels<S>(_ inputLabels: [S], isEnabled: Bool = true) -> some TabContent<Self.TabValue> where S : StringProtocol
```

## Discussion

Provide labels in descending order of importance. Voice Control and Full Keyboard Access use the input labels.

> **Note**: If you don’t specify any input labels, the user can still refer to the tab using the accessibility label that you add with the `accessibilityLabel()` modifier.

```swift
var body: some View {
    TabView {
        Tab {
            MessagesView()
        } label: {
            Image(systemName: "mail")
        }
        .accessibilityInputLabels(["Messages", "Mail", "Conversations"])
    }
}
```

## Parameters

- `inputLabelKeys`: The accessibility input labels to apply.
- `isEnabled`: If true the accessibility input labels are applied; otherwise the accessibility input labels are unchanged.

## See Also

### Configuring tab accessibility
- [func accessibilityHint(_:isEnabled:)](./accessibilityhint%28_,isenabled%29.md)
  Communicates to the user what happens after selecting the tab.
- [func accessibilityIdentifier(String, isEnabled: Bool) -> some TabContent<Self.TabValue>
](./accessibilityidentifier%28_,isenabled%29.md)
  Uses the string you specify to identify the view. Use this value for testing. It isn’t visible to the user.
- [func accessibilityLabel(_:isEnabled:)](./accessibilitylabel%28_,isenabled%29.md)
  Adds a label to the tab that describes its contents.
- [func accessibilityValue(_:isEnabled:)](./accessibilityvalue%28_,isenabled%29.md)
  Adds a textual description of the value that the tab contains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/accessibilityinputlabels(_:isenabled:))*