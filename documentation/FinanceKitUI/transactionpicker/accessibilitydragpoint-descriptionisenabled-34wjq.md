# accessibilityDragPoint(_:description:isEnabled:)

**Framework**: FinanceKitUI  
**Kind**: method

The point an assistive technology should use to begin a drag interaction.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
func accessibilityDragPoint<S>(_ point: UnitPoint, description: S, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier> where S : StringProtocol
```

#### Discussion

Use this modifier when you need to provide a description to users when prompted begin a drag interaction.

```None
struct FileView: View {
    var filename: String

    var body: some View {
        FileIcon(filename: filename)
            .accessibilityDragPoint(
                .center, description: Text("Move \(filename)"))
    }
}
```

By default, if an accessible view or its subtree has drag and/or drop interactions, they will be automatically exposed by assistive technologies. However, if there is more than one such interaction, each drag or drop should have a description to disambiguate it and give a good user experience.

> **Note**: An accessibility element can have multiple points for a drag, provided they have different descriptions.

An accessibility element can have multiple points for a drag, provided they have different descriptions.

## Parameters

- `point`: The point the assitive technology will begin a drag   interaction.
- `description`: The description of the drag interaction.
- `isEnabled`: If true the accessibility drag point is applied;   otherwise the accessibility drag point is unchanged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker/accessibilitydragpoint(_:description:isenabled:)-34wjq)*