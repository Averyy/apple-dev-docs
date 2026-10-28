# navigationBarTitle(_:displayMode:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the title and display mode in the navigation bar for this view.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`navigationTitle(_:)`](./navigationtitle%28_%29-avgj.md) with [`navigationBarTitleDisplayMode(_:)`](./navigationbartitledisplaymode%28_%29.md).

## Declaration

```swift
nonisolated
func navigationBarTitle<S>(_ title: S, displayMode: NavigationBarItem.TitleDisplayMode) -> some View where S : StringProtocol
```

**Other overloads**:

```swift
nonisolated
func navigationBarTitle(_ title: Text, displayMode: NavigationBarItem.TitleDisplayMode) -> some View
```

```swift
nonisolated
func navigationBarTitle(_ titleKey: LocalizedStringKey, displayMode: NavigationBarItem.TitleDisplayMode) -> some View
```

## Discussion

Use `navigationBarTitle(_:, displayMode)` to set the title of the navigation bar for this view and specify a display mode for the title from one of the `NavigationBarItem.Title.DisplayMode` styles. This modifier only takes effect when this view is inside of and visible within a `NavigationView`.

In the example below, `navigationBarTitle(_:, displayMode)` uses a string to provide a title for the navigation bar. Setting the title’s `displaymode` to `.inline` places the navigation bar title within the bounds of the navigation bar.

In the example below, text for the navigation bar title is provided using a string. The navigation bar title’s `displayMode` is set to `.inline` which places the navigation bar title in the bounds of the navigation bar.

```swift
struct FlavorView: View {
    let items = ["Chocolate", "Vanilla", "Strawberry", "Mint Chip",
                 "Pistachio"]
    let title = "Today's Flavors"
    var body: some View {
        NavigationView {
            List(items, id: \.self) {
                Text($0)
            }
            .navigationBarTitle(title, displayMode: .inline)
        }
    }
}
```

## Parameters

- `title`: A title for this view to display in the navigation bar.
- `displayMode`: The way to display the title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationbartitle(_:displaymode:)-5071t)*