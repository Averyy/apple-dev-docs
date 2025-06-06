# ControlGroup

**Framework**: SwiftUI  
**Kind**: struct

A container view that displays semantically-related controls in a visually-appropriate manner for the context

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct ControlGroup<Content> where Content : View
```

#### Overview

You can provide an optional label to this view that describes its children. This view may be used in different ways depending on the surrounding context. For example, when you place the control group in a toolbar item, SwiftUI uses the label when the group is moved to the toolbar’s overflow menu.

```swift
ContentView()
    .toolbar(id: "items") {
        ToolbarItem(id: "media") {
            ControlGroup {
                MediaButton()
                ChartButton()
                GraphButton()
            } label: {
                Label("Plus", systemImage: "plus")
            }
        }
    }
```

## Topics

### Creating a control group
- [init(content: () -> Content)](controlgroup/init(content:).md)
  Creates a new ControlGroup with the specified children
- [init<C, L>(content: () -> C, label: () -> L)](controlgroup/init(content:label:).md)
  Creates a new control group with the specified content and a label.
- [init(_:content:)](controlgroup/init(_:content:).md)
  Creates a new control group with the specified content that generates its label from a string.
### Creating a control group with an image
- [init(_:image:content:)](controlgroup/init(_:image:content:).md)
  Creates a new control group with the specified content that generates its label from a string and image name.
- [init(_:systemImage:content:)](controlgroup/init(_:systemimage:content:).md)
  Creates a new control group with the specified content that generates its label from a string and image name.
### Creating a configured control group
- [init(ControlGroupStyleConfiguration)](controlgroup/init(_:).md)
  Creates a control group based on a style configuration.
### Supporting types
- [struct LabeledControlGroupContent](labeledcontrolgroupcontent.md)
  A view that represents the body of a control group with a specified label.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [func controlGroupStyle<S>(S) -> some View](view/controlgroupstyle(_:).md)
  Sets the style for control groups within this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/controlgroup)*