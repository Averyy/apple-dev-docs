# navigationBarTitle(_:displayMode:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the title and display mode in the navigation bar for this view.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`navigationTitle(_:)`](./navigationtitle%28_%29-43srq.md) with [`navigationBarTitleDisplayMode(_:)`](./navigationbartitledisplaymode%28_%29.md).

## Declaration

```swift
nonisolated
func navigationBarTitle(_ titleKey: LocalizedStringKey, displayMode: NavigationBarItem.TitleDisplayMode) -> some View
```

**Other overloads**:

```swift
nonisolated
func navigationBarTitle(_ title: Text, displayMode: NavigationBarItem.TitleDisplayMode) -> some View
```

```swift
nonisolated
func navigationBarTitle<S>(_ title: S, displayMode: NavigationBarItem.TitleDisplayMode) -> some View where S : StringProtocol
```

## Discussion

Use `navigationBarTitle(_:displayMode:)` to set the title of the navigation bar for this view and specify a display mode for the title from one of the [`NavigationBarItem.TitleDisplayMode`](../navigationbaritem/titledisplaymode.md) styles. This modifier only takes effect when this view is inside of and visible within a [`NavigationView`](../navigationview.md).

In the example below, text for the navigation bar title is provided using a string. The navigation bar title’s [`NavigationBarItem.TitleDisplayMode`](../navigationbaritem/titledisplaymode.md) is set to `.inline` which places the navigation bar title in the bounds of the navigation bar.

```swift
struct FlavorView: View {
    let items = ["Chocolate", "Vanilla", "Strawberry", "Mint Chip",
                 "Pistachio"]
    var body: some View {
        NavigationView {
            List(items, id: \.self) {
                Text($0)
            }
            .navigationBarTitle("Today's Flavors", displayMode: .inline)
        }
    }
}
```

If the `titleKey` can’t be found, the title uses the text of the key name instead.

## Parameters

- `titleKey`: A key to a localized description of this view to display in the navigation bar.
- `displayMode`: The style to use for displaying the navigation bar title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/navigationbartitle(_:displaymode:)-gi7a)*