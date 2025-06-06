# accessibilityDropPoint(_:description:)

**Framework**: App Intents  
**Kind**: method

The point an assistive technology should use to end a drag interaction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func accessibilityDropPoint<S>(_ point: UnitPoint, description: S) -> ModifiedContent<Self, AccessibilityAttachmentModifier> where S : StringProtocol
```

#### Discussion

Use this modifier when you need to provide a description to users when prompted end a drag interaction.

```swift
struct FolderView: View {
    var folderName: String

    var body: some View {
        FolderIcon(folderName: folderName)
            .accessibilityDropPoint(.center, description: "Move to \(folderName)")
    }
}
```

By default, if an accessible view or its subtree has drag and/or drop interactions, they will be automatically exposed by assistive technologies. However, if there is more than one such interaction, each drag or drop should have a description to disambiguate it and give a good user experience.

> **Note**: An accessibility element can have multiple points for a drop, provided they have different descriptions.

An accessibility element can have multiple points for a drop, provided they have different descriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/accessibilitydroppoint(_:description:)-4hnam)*