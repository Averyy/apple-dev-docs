# navigationViewStyle(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the style for navigation views within this view.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: Replace a styled [`NavigationView`](../navigationview.md) with a [`NavigationStack`](../navigationstack.md) or [`NavigationSplitView`](../navigationsplitview.md). For more information, see [Migrating to new navigation types](../migrating-to-new-navigation-types.md).

## Declaration

```swift
nonisolated
func navigationViewStyle<S>(_ style: S) -> some View where S : NavigationViewStyle
```

## Discussion

Use this modifier to change the appearance and behavior of navigation views. For example, by default, navigation views appear with multiple columns in wider environments, like iPad in landscape orientation:

![A screenshot of an iPad in landscape orientation mode showing a](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/View-navigationViewStyle-1@2x.png)

You can apply the [`stack`](../navigationviewstyle/stack.md) style to force single-column stack navigation in these environments:

```swift
NavigationView {
    List {
        NavigationLink("Purple", destination: ColorDetail(color: .purple))
        NavigationLink("Pink", destination: ColorDetail(color: .pink))
        NavigationLink("Orange", destination: ColorDetail(color: .orange))
    }
    .navigationTitle("Colors")

    Text("Select a Color") // A placeholder to show before selection.
}
.navigationViewStyle(.stack)
```

![A screenshot of an iPad in landscape orientation mode showing a single column containing the list Purple, Pink, and Orange.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/View-navigationViewStyle-2@2x.png)

## See Also

### Styling navigation views
- [protocol NavigationViewStyle](../navigationviewstyle.md)
  A specification for the appearance and interaction of a navigation view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationviewstyle(_:))*