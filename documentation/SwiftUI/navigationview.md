# NavigationView

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A view for presenting a stack of views that represents a visible path in a navigation hierarchy.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: Use [`NavigationStack`](./navigationstack.md) and [`NavigationSplitView`](./navigationsplitview.md) instead. For more information, see [Migrating to new navigation types](./migrating-to-new-navigation-types.md).

## Declaration

```swift
nonisolated
struct NavigationView<Content> where Content : View
```

## Mentions

- [Migrating to new navigation types](./migrating-to-new-navigation-types.md)
- [Picking container views for your content](./picking-container-views-for-your-content.md)

#### Overview

Use a `NavigationView` to create a navigation-based app in which the user can traverse a collection of views. Users navigate to a destination view by selecting a [`NavigationLink`](./navigationlink.md) that you provide. On iPadOS and macOS, the destination content appears in the next column. Other platforms push a new view onto the stack, and enable removing items from the stack with platform-specific controls, like a Back button or a swipe gesture.

![A diagram showing a multicolumn navigation view on macOS, and a stack of views on iOS.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/NavigationView-1@2x.png)

Use the [`init(content:)`](./navigationview/init%28content%29.md) initializer to create a navigation view that directly associates navigation links and their destination views:

```swift
NavigationView {
    List(model.notes) { note in
        NavigationLink(note.title, destination: NoteEditor(id: note.id))
    }
    Text("Select a Note")
}
```

Style a navigation view by modifying it with the [`navigationViewStyle(_:)`](./view/navigationviewstyle%28_%29.md) view modifier. Use other modifiers, like [`navigationTitle(_:)`](./view/navigationtitle%28_%29-avgj.md), on views presented by the navigation view to customize the navigation interface for the presented view.

## Topics

### Creating a navigation view
- [init(content: () -> Content)](./navigationview/init%28content%29.md)
  Creates a destination-based navigation view.
### Styling navigation views
- [func navigationViewStyle<S>(S) -> some View](./view/navigationviewstyle%28_%29.md)
  Sets the style for navigation views within this view.
- [protocol NavigationViewStyle](./navigationviewstyle.md)
  A specification for the appearance and interaction of a navigation view.

## Relationships

### Conforms To
- [View](./view.md)

## See Also

### Presenting views in columns
- [Bringing robust navigation structure to your SwiftUI app](./bringing-robust-navigation-structure-to-your-swiftui-app.md)
  Use navigation links, stacks, destinations, and paths to provide a streamlined experience for all platforms, as well as behaviors such as deep linking and state restoration.
- [Migrating to new navigation types](./migrating-to-new-navigation-types.md)
  Improve navigation behavior in your app by replacing navigation views with navigation stacks and navigation split views.
- [struct NavigationSplitView](./navigationsplitview.md)
  A view that presents views in two or three columns, where selections in leading columns control presentations in subsequent columns.
- [func navigationSplitViewStyle<S>(S) -> some View](./view/navigationsplitviewstyle%28_%29.md)
  Sets the style for navigation split views within this view.
- [func navigationSplitViewColumnWidth(CGFloat) -> some View](./view/navigationsplitviewcolumnwidth%28_%29.md)
  Sets a fixed, preferred width for the column containing this view.
- [func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) -> some View](./view/navigationsplitviewcolumnwidth%28min,ideal,max%29.md)
  Sets a flexible, preferred width for the column containing this view.
- [struct NavigationSplitViewVisibility](./navigationsplitviewvisibility.md)
  The visibility of the leading columns in a navigation split view.
- [struct NavigationLink](./navigationlink.md)
  A view that controls a navigation presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationview)*