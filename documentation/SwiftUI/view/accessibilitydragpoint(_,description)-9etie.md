# accessibilityDragPoint(_:description:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

The point an assistive technology should use to begin a drag interaction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func accessibilityDragPoint(_ point: UnitPoint, description: LocalizedStringKey) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func accessibilityDragPoint(_ point: UnitPoint, description: LocalizedStringResource) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

```swift
nonisolated
func accessibilityDragPoint(_ point: UnitPoint, description: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

```swift
nonisolated
func accessibilityDragPoint<S>(_ point: UnitPoint, description: S) -> ModifiedContent<Self, AccessibilityAttachmentModifier> where S : StringProtocol
```

## Discussion

Use this modifier when you need to provide a description to users when prompted begin a drag interaction.

```swift
struct FileView: View {
    var filename: String

    var body: some View {
        FileIcon(filename: filename)
            .accessibilityDragPoint(.center, description: "Move \(filename)")
    }
}
```

By default, if an accessible view or its subtree has drag and/or drop interactions, they will be automatically exposed by assistive technologies. However, if there is more than one such interaction, each drag or drop should have a description to disambiguate it and give a good user experience.

> **Note**: An accessibility element can have multiple points for a drag, provided they have different descriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/accessibilitydragpoint(_:description:)-9etie)*