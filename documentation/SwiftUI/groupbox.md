# GroupBox

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A stylized view, with an optional label, that visually collects a logical grouping of content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
nonisolated
struct GroupBox<Label, Content> where Label : View, Content : View
```

## Overview

Use a group box when you want to visually distinguish a portion of your user interface with an optional title for the boxed content.

The following example sets up a `GroupBox` with the label “End-User Agreement”, and a long `agreementText` string in a [`Text`](./text.md) view wrapped by a [`ScrollView`](./scrollview.md). The box also contains a [`Toggle`](./toggle.md) for the user to interact with after reading the text.

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

![An iOS status bar above a gray rounded rectangle region marking the bounds](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-GroupBox-EULA@2x.png)

## Topics

### Creating a group box
- [init(content: () -> Content)](./groupbox/init%28content%29.md)
  Creates an unlabeled group box with the provided view content.
- [init(content: () -> Content, label: () -> Label)](./groupbox/init%28content,label%29.md)
  Creates a group box with the provided label and view content.
- [init(_:content:)](./groupbox/init%28_,content%29.md)
  Creates a group box with the provided view content and title.
- [init(label: Label, content: () -> Content)](./groupbox/init%28label,content%29.md)
### Creating a group box from a configuration
- [init(GroupBoxStyleConfiguration)](./groupbox/init%28_%29.md)
  Creates a group box based on a style configuration.

## Relationships

### Conforms To
- [View](./view.md)

## See Also

### Grouping views into a box
- [func groupBoxStyle<S>(S) -> some View](./view/groupboxstyle%28_%29.md)
  Sets the style for group boxes within this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/groupbox)*