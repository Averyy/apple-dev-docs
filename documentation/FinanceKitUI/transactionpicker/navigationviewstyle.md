# navigationViewStyle(_:)

**Framework**: FinanceKitUI  
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

#### Discussion

Use this modifier to change the appearance and behavior of navigation views. For example, by default, navigation views appear with multiple columns in wider environments, like iPad in landscape orientation:

You can apply the `NavigationViewStyle/stack` style to force single-column stack navigation in these environments:

```None
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker/navigationviewstyle(_:))*