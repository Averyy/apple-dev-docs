# help(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds help text to a view using a localized string that you provide.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func help(_ textKey: LocalizedStringKey) -> some View
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func help(_ textKey: LocalizedStringResource) -> some View
```

```swift
nonisolated
func help(_ text: Text) -> some View
```

```swift
nonisolated
func help<S>(_ text: S) -> some View where S : StringProtocol
```

## Discussion

Adding help to a view configures the view’s accessibility hint and its help tag (also called a *tooltip*) in macOS or visionOS. For more information on using help tags, see [Offering help](https://developer.apple.com/design/human-interface-guidelines/offering-help) in the Human Interface Guidelines.

```swift
Button(action: composeMessage) {
    Image(systemName: "square.and.pencil")
}
.help("Compose a new message")
```

## Parameters

- `textKey`: The key for the localized text to use as help.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/help(_:)-4y7cy)*