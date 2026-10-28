# accessibilityHint(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Communicates to the user what happens after performing the view’s action.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@export(implementation)
nonisolated func accessibilityHint(_ hint: LocalizedStringResource) -> ModifiedContent<Content, Modifier>
```

Available when `Modifier` is `AccessibilityAttachmentModifier`.

**Other overloads**:

```swift
nonisolated
func accessibilityHint(_ hint: Text) -> ModifiedContent<Content, Modifier>
```

```swift
nonisolated
func accessibilityHint(_ hintKey: LocalizedStringKey) -> ModifiedContent<Content, Modifier>
```

```swift
nonisolated
func accessibilityHint<S>(_ hint: S) -> ModifiedContent<Content, Modifier> where S : StringProtocol
```

## Discussion

Provide a hint in the form of a brief phrase, like “Purchases the item” or “Downloads the attachment”.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/modifiedcontent/accessibilityhint(_:))*