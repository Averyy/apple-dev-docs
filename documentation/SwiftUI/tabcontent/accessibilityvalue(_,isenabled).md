# accessibilityValue(_:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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
@export(implementation)
nonisolated func accessibilityValue(_ valueResource: LocalizedStringResource, isEnabled: Bool = true) -> some TabContent<Self.TabValue>
```

**Other overloads**:

```swift
nonisolated
func accessibilityValue(_ valueDescription: Text, isEnabled: Bool = true) -> some TabContent<Self.TabValue>
```

```swift
nonisolated
func accessibilityValue(_ valueKey: LocalizedStringKey, isEnabled: Bool = true) -> some TabContent<Self.TabValue>
```

```swift
nonisolated
func accessibilityValue<S>(_ value: S, isEnabled: Bool = true) -> some TabContent<Self.TabValue> where S : StringProtocol
```

## Discussion

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

- `valueResource`: The accessibility value to apply.
- `isEnabled`: If true the accessibility value is applied; otherwise the accessibility value is unchanged.

## See Also

### Configuring tab accessibility
- [func accessibilityHint(_:isEnabled:)](./accessibilityhint%28_,isenabled%29.md)
  Communicates to the user what happens after selecting the tab.
- [func accessibilityIdentifier(String, isEnabled: Bool) -> some TabContent<Self.TabValue>
](./accessibilityidentifier%28_,isenabled%29.md)
  Uses the string you specify to identify the view. Use this value for testing. It isn’t visible to the user.
- [func accessibilityInputLabels(_:isEnabled:)](./accessibilityinputlabels%28_,isenabled%29.md)
  Sets alternate input labels with which users identify a tab.
- [func accessibilityLabel(_:isEnabled:)](./accessibilitylabel%28_,isenabled%29.md)
  Adds a label to the tab that describes its contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/accessibilityvalue(_:isenabled:))*