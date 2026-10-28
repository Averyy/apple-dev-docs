# accessibilityInputLabels(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets alternate input labels with which users identify a view.

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
func accessibilityInputLabels(_ inputLabels: [Text]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

**Other overloads**:

```swift
nonisolated
func accessibilityInputLabels(_ inputLabelKeys: [LocalizedStringKey]) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

```swift
nonisolated
func accessibilityInputLabels<S>(_ inputLabels: [S]) -> ModifiedContent<Self, AccessibilityAttachmentModifier> where S : StringProtocol
```

## Discussion

Provide labels in descending order of importance. Voice Control and Full Keyboard Access use the input labels.

> **Note**: If you don’t specify any input labels, the user can still refer to the view using the accessibility label that you add with the `accessibilityLabel()` modifier.

## Parameters

- `inputLabels`: An array of Text elements to use as input labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/accessibilityinputlabels(_:)-9q3yf)*