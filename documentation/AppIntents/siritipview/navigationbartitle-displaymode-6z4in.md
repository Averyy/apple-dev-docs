# navigationBarTitle(_:displayMode:)

**Framework**: App Intents  
**Kind**: method

Sets the title and display mode in the navigation bar for this view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func navigationBarTitle<S>(_ title: S, displayMode: NavigationBarItem.TitleDisplayMode) -> some View where S : StringProtocol
```

#### Discussion

Use `navigationBarTitle(_:displayMode:)` to set the title of the navigation bar for this view and specify a display mode for the title from one of the `NavigationBarItem.Title.DisplayMode` styles. This modifier only takes effect when this view is inside of and visible within a `NavigationView`.

In the example below, `navigationBarTitle(_:displayMode:)` uses a string to provide a title for the navigation bar. Setting the title’s `displayMode` to `.inline` places the navigation bar title within the bounds of the navigation bar.

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

![A screenshot of a navigation bar, showing the title within the bounds of the navigation bar] (SwiftUI-navigationBarTitle-stringProtocol.png)

## Parameters

- `title`: A title for this view to display in the navigation bar.
- `displayMode`: The way to display the title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/navigationbartitle(_:displaymode:)-6z4in)*