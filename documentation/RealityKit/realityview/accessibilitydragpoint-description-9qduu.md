# accessibilityDragPoint(_:description:)

**Framework**: Realitykit  
**Kind**: method

The point an assistive technology should use to begin a drag interaction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- visionOS ?+

## Declaration

```swift
nonisolated
func accessibilityDragPoint(_ point: UnitPoint, description: Text) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Use this modifier when you need to provide a description to users when prompted begin a drag interaction.

```None
struct FileView: View {
    var filename: String

    var body: some View {
        FileIcon(filename: filename)
            .accessibilityDragPoint(.center, description: Text("Move \(filename)"))
    }
}
```

By default, if an accessible view or its subtree has drag and/or drop interactions, they will be automatically exposed by assistive technologies. However, if there is more than one such interaction, each drag or drop should have a description to disambiguate it and give a good user experience.

> **Note**: An accessibility element can have multiple points for a drag, provided they have different descriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/accessibilitydragpoint(_:description:)-9qduu)*