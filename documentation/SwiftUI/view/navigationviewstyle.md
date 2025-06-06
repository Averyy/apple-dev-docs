# navigationViewStyle(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the style for navigation views within this view.

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
nonisolated
func navigationViewStyle<S>(_ style: S) -> some View where S : NavigationViewStyle
```

## Mentions

- [Displaying data in lists](displaying-data-in-lists.md)

#### Discussion

Use this modifier to change the appearance and behavior of navigation views. For example, by default, navigation views appear with multiple columns in wider environments, like iPad in landscape orientation:

![A screenshot of an iPad in landscape orientation mode showing a](https://docs-assets.developer.apple.com/published/6ea0c512dea9061acb17a64140b660e6/View-navigationViewStyle-1%402x.png)

You can apply the [`stack`](navigationviewstyle/stack.md) style to force single-column stack navigation in these environments:

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

![A screenshot of an iPad in landscape orientation mode showing a single column containing the list Purple, Pink, and Orange.](https://docs-assets.developer.apple.com/published/5df851308e1be644de4f133b0780d285/View-navigationViewStyle-2%402x.png)

## See Also

- [protocol NavigationViewStyle](navigationviewstyle.md)
  A specification for the appearance and interaction of a navigation view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationviewstyle(_:))*