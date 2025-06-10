# navigationBarTitle(_:displayMode:)

**Framework**: App Intents  
**Kind**: method

Sets the title and display mode in the navigation bar for this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func navigationBarTitle(_ titleKey: LocalizedStringKey, displayMode: NavigationBarItem.TitleDisplayMode) -> some View
```

#### Discussion

Use `navigationBarTitle(_:displayMode:)` to set the title of the navigation bar for this view and specify a display mode for the title from one of the `NavigationBarItem/TitleDisplayMode` styles. This modifier only takes effect when this view is inside of and visible within a `NavigationView`.

In the example below, text for the navigation bar title is provided using a string. The navigation bar title’s `NavigationBarItem/TitleDisplayMode` is set to `.inline` which places the navigation bar title in the bounds of the navigation bar.

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

- `titleKey`: A key to a localized description of this view to display   in the navigation bar.
- `displayMode`: The style to use for displaying the navigation bar   title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/navigationbartitle(_:displaymode:)-93ls3)*