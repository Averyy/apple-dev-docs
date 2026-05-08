# EditButton

**Framework**: SwiftUI  
**Kind**: struct

A button that toggles the edit mode environment value.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
struct EditButton
```

#### Overview

An edit button toggles the environment’s [`editMode`](environmentvalues/editmode.md) value for content within a container that supports edit mode. In the following example, an edit button placed inside a [`NavigationView`](navigationview.md) supports editing of a [`List`](list.md):

```swift
@State private var fruits = [
    "Apple",
    "Banana",
    "Papaya",
    "Mango"
]

var body: some View {
    NavigationView {
        List {
            ForEach(fruits, id: \.self) { fruit in
                Text(fruit)
            }
            .onDelete { fruits.remove(atOffsets: $0) }
            .onMove { fruits.move(fromOffsets: $0, toOffset: $1) }
        }
        .navigationTitle("Fruits")
        .toolbar {
            EditButton()
        }
    }
}
```

Because the [`ForEach`](foreach.md) in the above example defines behaviors for [`onDelete(perform:)`](dynamicviewcontent/ondelete(perform:).md) and [`onMove(perform:)`](dynamicviewcontent/onmove(perform:).md), the editable list displays the delete and move UI when the user taps Edit. Notice that the Edit button displays the title “Done” while edit mode is active:

![A screenshot of an app with an Edit button in the navigation bar.](https://docs-assets.developer.apple.com/published/ef01598c8da781c8c60c9e3bcaa97418/EditButton-1%402x.png)

You can also create custom views that react to changes in the edit mode state, as described in [`EditMode`](editmode.md).

## Topics

### Creating an edit button
- [init()](editbutton/init.md)
  Creates an Edit button instance.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [struct PasteButton](pastebutton.md)
  A system button that reads items from the pasteboard and delivers it to a closure.
- [struct RenameButton](renamebutton.md)
  A button that triggers a standard rename action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/editbutton)*