# navigationSplitViewStyle(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the style for navigation split views within this view.

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
nonisolated
func navigationSplitViewStyle<S>(_ style: S) -> some View where S : NavigationSplitViewStyle
```

## Mentions

- [Migrating to new navigation types](migrating-to-new-navigation-types.md)

#### Return Value

A view that uses the specified navigation split view style.

## Parameters

- `style`: The style to set.

## See Also

- [Bringing robust navigation structure to your SwiftUI app](bringing-robust-navigation-structure-to-your-swiftui-app.md)
  Use navigation links, stacks, destinations, and paths to provide a streamlined experience for all platforms, as well as behaviors such as deep linking and state restoration.
- [Migrating to new navigation types](migrating-to-new-navigation-types.md)
  Improve navigation behavior in your app by replacing navigation views with navigation stacks and navigation split views.
- [struct NavigationSplitView](navigationsplitview.md)
  A view that presents views in two or three columns, where selections in leading columns control presentations in subsequent columns.
- [func navigationSplitViewColumnWidth(CGFloat) -> some View](view/navigationsplitviewcolumnwidth(_:).md)
  Sets a fixed, preferred width for the column containing this view.
- [func navigationSplitViewColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) -> some View](view/navigationsplitviewcolumnwidth(min:ideal:max:).md)
  Sets a flexible, preferred width for the column containing this view.
- [struct NavigationSplitViewVisibility](navigationsplitviewvisibility.md)
  The visibility of the leading columns in a navigation split view.
- [struct NavigationLink](navigationlink.md)
  A view that controls a navigation presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationsplitviewstyle(_:))*