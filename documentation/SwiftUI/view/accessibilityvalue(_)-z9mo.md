# accessibilityValue(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds a textual description of the value that the view contains.

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
func accessibilityValue(_ valueDescription: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func accessibilityValue(_ valueResource: LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

```swift
nonisolated
func accessibilityValue(_ valueKey: LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

```swift
nonisolated
func accessibilityValue<S>(_ value: S) -> ModifiedContent<Self, AccessibilityAttachmentModifier> where S : StringProtocol
```

## Discussion

Use this method to describe the value represented by a view, but only if that’s different than the view’s label. For example, for a slider that you label as “Volume” using accessibilityLabel(), you can provide the current volume setting, like “60%”, using accessibilityValue().


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/accessibilityvalue(_:)-z9mo)*