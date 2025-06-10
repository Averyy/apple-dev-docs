# NavigationSplitViewVisibility

**Framework**: SwiftUI  
**Kind**: struct

The visibility of the leading columns in a navigation split view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct NavigationSplitViewVisibility
```

#### Overview

Use a value of this type to control the visibility of the columns of a [`NavigationSplitView`](navigationsplitview.md). Create a [`State`](state.md) property with a value of this type, and pass a [`Binding`](binding.md) to that state to the [`init(columnVisibility:sidebar:detail:)`](navigationsplitview/init(columnvisibility:sidebar:detail:).md) or [`init(columnVisibility:sidebar:content:detail:)`](navigationsplitview/init(columnvisibility:sidebar:content:detail:).md) initializer when you create the navigation split view. You can then modify the value elsewhere in your code to:

- Hide all but the trailing column with [`detailOnly`](navigationsplitviewvisibility/detailonly.md).
- Hide the leading column of a three-column navigation split view with [`doubleColumn`](navigationsplitviewvisibility/doublecolumn.md).
- Show all the columns with [`all`](navigationsplitviewvisibility/all.md).
- Rely on the automatic behavior for the current context with [`automatic`](navigationsplitviewvisibility/automatic.md).

> **Note**: Some platforms don’t respect every option. For example, macOS always displays the content column.

## Topics

### Getting visibilities
- [static var automatic: NavigationSplitViewVisibility](navigationsplitviewvisibility/automatic.md)
  Use the default leading column visibility for the current device.
- [static var all: NavigationSplitViewVisibility](navigationsplitviewvisibility/all.md)
  Show all the columns of a three-column navigation split view.
- [static var doubleColumn: NavigationSplitViewVisibility](navigationsplitviewvisibility/doublecolumn.md)
  Show the content column and detail area of a three-column navigation split view, or the sidebar column and detail area of a two-column navigation split view.
- [static var detailOnly: NavigationSplitViewVisibility](navigationsplitviewvisibility/detailonly.md)
  Hide the leading two columns of a three-column navigation split view, so that just the detail area shows.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Bringing robust navigation structure to your SwiftUI app](bringing-robust-navigation-structure-to-your-swiftui-app.md)
  Use navigation links, stacks, destinations, and paths to provide a streamlined experience for all platforms, as well as behaviors such as deep linking and state restoration.
- [Migrating to new navigation types](migrating-to-new-navigation-types.md)
  Improve navigation behavior in your app by replacing navigation views with navigation stacks and navigation split views.
- [struct NavigationSplitView](navigationsplitview.md)
  A view that presents views in two or three columns, where selections in leading columns control presentations in subsequent columns.
- [func navigationSplitViewStyle<S>(S) -> some View](view/navigationsplitviewstyle(_:).md)
  Sets the style for navigation split views within this view.
- [func navigationSplitViewColumnWidth(CGFloat) -> some View](view/navigationsplitviewcolumnwidth(_:).md)
  Sets a fixed, preferred width for the column containing this view.
- [func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) -> some View](view/navigationsplitviewcolumnwidth(min:ideal:max:).md)
  Sets a flexible, preferred width for the column containing this view.
- [struct NavigationLink](navigationlink.md)
  A view that controls a navigation presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationsplitviewvisibility)*