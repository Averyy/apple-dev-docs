# accessibilityHint(_:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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
@export(implementation)
nonisolated func accessibilityHint(_ hint: LocalizedStringResource, isEnabled: Bool = true) -> some TabContent<Self.TabValue>
```

**Other overloads**:

```swift
nonisolated
func accessibilityHint(_ hint: Text, isEnabled: Bool = true) -> some TabContent<Self.TabValue>
```

```swift
nonisolated
func accessibilityHint(_ hintKey: LocalizedStringKey, isEnabled: Bool = true) -> some TabContent<Self.TabValue>
```

```swift
nonisolated
func accessibilityHint<S>(_ hint: S, isEnabled: Bool = true) -> some TabContent<Self.TabValue> where S : StringProtocol
```

## Discussion

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

### Configuring tab accessibility
- [func accessibilityIdentifier(String, isEnabled: Bool) -> some TabContent<Self.TabValue>
](./accessibilityidentifier%28_,isenabled%29.md)
  Uses the string you specify to identify the view. Use this value for testing. It isn’t visible to the user.
- [func accessibilityInputLabels(_:isEnabled:)](./accessibilityinputlabels%28_,isenabled%29.md)
  Sets alternate input labels with which users identify a tab.
- [func accessibilityLabel(_:isEnabled:)](./accessibilitylabel%28_,isenabled%29.md)
  Adds a label to the tab that describes its contents.
- [func accessibilityValue(_:isEnabled:)](./accessibilityvalue%28_,isenabled%29.md)
  Adds a textual description of the value that the tab contains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/accessibilityhint(_:isenabled:))*