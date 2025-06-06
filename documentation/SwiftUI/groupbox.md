# GroupBox

**Framework**: SwiftUI  
**Kind**: struct

A stylized view, with an optional label, that visually collects a logical grouping of content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
struct GroupBox<Label, Content> where Label : View, Content : View
```

#### Overview

Use a group box when you want to visually distinguish a portion of your user interface with an optional title for the boxed content.

The following example sets up a `GroupBox` with the label “End-User Agreement”, and a long `agreementText` string in a [`Text`](text.md) view wrapped by a [`ScrollView`](scrollview.md). The box also contains a [`Toggle`](toggle.md) for the user to interact with after reading the text.

```swift
var body: some View {
    GroupBox(label:
        Label("End-User Agreement", systemImage: "building.columns")
    ) {
        ScrollView(.vertical, showsIndicators: true) {
            Text(agreementText)
                .font(.footnote)
        }
        .frame(height: 100)
        Toggle(isOn: $userAgreed) {
            Text("I agree to the above terms")
        }
    }
}
```

![An iOS status bar above a gray rounded rectangle region marking the bounds](https://docs-assets.developer.apple.com/published/30caaa19222a89d8e8c721f916f1003a/SwiftUI-GroupBox-EULA%402x.png)

## Topics

### Creating a group box
- [init(content: () -> Content)](groupbox/init(content:).md)
  Creates an unlabeled group box with the provided view content.
- [init(content: () -> Content, label: () -> Label)](groupbox/init(content:label:).md)
  Creates a group box with the provided label and view content.
- [init(_:content:)](groupbox/init(_:content:).md)
  Creates a group box with the provided view content and title.
### Creating a group box from a configuration
- [init(GroupBoxStyleConfiguration)](groupbox/init(_:).md)
  Creates a group box based on a style configuration.
### Deprecated initializers
- [init(label: Label, content: () -> Content)](groupbox/init(label:content:).md)

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [func groupBoxStyle<S>(S) -> some View](view/groupboxstyle(_:).md)
  Sets the style for group boxes within this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/groupbox)*