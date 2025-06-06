# NavigationView

**Framework**: SwiftUI  
**Kind**: struct

A view for presenting a stack of views that represents a visible path in a navigation hierarchy.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
struct NavigationView<Content> where Content : View
```

## Mentions

- [Migrating to new navigation types](migrating-to-new-navigation-types.md)
- [Picking container views for your content](picking-container-views-for-your-content.md)
- [Displaying data in lists](displaying-data-in-lists.md)

#### Overview

Use a `NavigationView` to create a navigation-based app in which the user can traverse a collection of views. Users navigate to a destination view by selecting a [`NavigationLink`](navigationlink.md) that you provide. On iPadOS and macOS, the destination content appears in the next column. Other platforms push a new view onto the stack, and enable removing items from the stack with platform-specific controls, like a Back button or a swipe gesture.

![A diagram showing a multicolumn navigation view on macOS, and a stack of views on iOS.](https://docs-assets.developer.apple.com/published/fca0c98e5ab89310dea5abd6e14697cc/NavigationView-1%402x.png)

Use the [`init(content:)`](navigationview/init(content:).md) initializer to create a navigation view that directly associates navigation links and their destination views:

```swift
NavigationView {
    List(model.notes) { note in
        NavigationLink(note.title, destination: NoteEditor(id: note.id))
    }
    Text("Select a Note")
}
```

Style a navigation view by modifying it with the [`navigationViewStyle(_:)`](view/navigationviewstyle(_:).md) view modifier. Use other modifiers, like [`navigationTitle(_:)`](view/navigationtitle(_:)-avgj.md), on views presented by the navigation view to customize the navigation interface for the presented view.

## Topics

### Creating a navigation view
- [init(content: () -> Content)](navigationview/init(content:).md)
  Creates a destination-based navigation view.
### Styling navigation views
- [func navigationViewStyle<S>(S) -> some View](view/navigationviewstyle(_:).md)
  Sets the style for navigation views within this view.
- [protocol NavigationViewStyle](navigationviewstyle.md)
  A specification for the appearance and interaction of a navigation view.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [func tabItem<V>(() -> V) -> some View](view/tabitem(_:).md)
  Sets the tab bar item associated with this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationview)*