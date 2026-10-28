# accessibilityInputLabels(_:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets alternate input labels with which users identify a view.

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
func accessibilityInputLabels<S>(_ inputLabels: [S], isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier> where S : StringProtocol
```

**Other overloads**:

```swift
nonisolated
func accessibilityInputLabels(_ inputLabelKeys: [LocalizedStringKey], isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

```swift
nonisolated
func accessibilityInputLabels(_ inputLabels: [Text], isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

## Discussion

Provide labels in descending order of importance. Voice Control and Full Keyboard Access use the input labels.

> **Note**: If you don’t specify any input labels, the user can still refer to the view using the accessibility label that you add with the `accessibilityLabel()` modifier.

## Parameters

- `inputLabels`: The accessibility input labels to apply.
- `isEnabled`: If true the accessibility input labels are applied; otherwise the accessibility input labels are unchanged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/accessibilityinputlabels(_:isenabled:)-3kx0v)*