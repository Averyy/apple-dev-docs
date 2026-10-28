# help(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds help text to a tab using a string that you provide.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
nonisolated
func help<S>(_ text: S) -> some TabContent<Self.TabValue> where S : StringProtocol
```

**Other overloads**:

```swift
nonisolated
func help(_ text: Text) -> some TabContent<Self.TabValue>
```

```swift
nonisolated
func help(_ textKey: LocalizedStringKey) -> some TabContent<Self.TabValue>
```

```swift
nonisolated
func help(_ textResource: LocalizedStringResource) -> some TabContent<Self.TabValue>
```

## Discussion

Adding help to a tab configures the tab’s accessibility hint and its help tag (also called a *tooltip*) in macOS or visionOS. For more information on using help tags, see [Offering help](https://developer.apple.com/design/human-interface-guidelines/offering-help) in the Human Interface Guidelines.

```swift
TabView {
    Tab("List", systemImage: "list.dash") {
        ListView()
    }
    .help("Display symbols in list format")
}
```

## Parameters

- `text`: The text to use as help.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/help(_:)-4khr5)*