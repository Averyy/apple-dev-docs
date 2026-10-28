# accessibilityAction(named:_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func accessibilityAction(named name: Text, _ handler: @escaping () -> Void) -> ModifiedContent<Content, Modifier>
```

Available when `Modifier` is `AccessibilityAttachmentModifier`.

**Other overloads**:

```swift
@export(implementation)
nonisolated func accessibilityAction(named nameResource: LocalizedStringResource, _ handler: @escaping () -> Void) -> ModifiedContent<Content, Modifier>
```

```swift
nonisolated
func accessibilityAction(named nameKey: LocalizedStringKey, _ handler: @escaping () -> Void) -> ModifiedContent<Content, Modifier>
```

```swift
nonisolated
func accessibilityAction<S>(named name: S, _ handler: @escaping () -> Void) -> ModifiedContent<Content, Modifier> where S : StringProtocol
```

## Discussion

For example, this is how a custom action to compose a new email could be added to a view.

```swift
var body: some View {
    ContentView()
        .accessibilityAction(named: Text("New Message")) {
            // Handle action
        }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibilityaction(named:_:)-4ji9i)*