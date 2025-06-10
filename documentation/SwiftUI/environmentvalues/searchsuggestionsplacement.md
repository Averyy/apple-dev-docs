# searchSuggestionsPlacement

**Framework**: SwiftUI  
**Kind**: property

The current placement of search suggestions.

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
var searchSuggestionsPlacement: SearchSuggestionsPlacement { get }
```

#### Discussion

Search suggestions render based on the platform and surrounding context in which you place the searchable modifier containing suggestions. You can render search suggestions in two ways:

- In a menu attached to the search field.
- Inline with the main content of the app.

You find the current search suggestion placement by querying the [`searchSuggestionsPlacement`](environmentvalues/searchsuggestionsplacement.md) in your search suggestions.

```swift
enum FruitSuggestion: String, Identifiable {
    case apple, banana, orange
    var id: Self { self }
}

@State private var text: String = ""
@State private var suggestions: [FruitSuggestion] = []

var body: some View {
    MainContent()
        .searchable(text: $text) {
            FruitSuggestions(suggestions: suggestions)
        }
}

struct FruitSuggestions: View {
    var suggestions: [FruitSuggestion]

    @Environment(\.searchSuggestionsPlacement)
    private var placement

    var body: some View {
        if shouldRender {
            ForEach(suggestions) { suggestion in
                Text(suggestion.rawValue.capitalized)
                    .searchCompletion(suggestion.rawValue)
            }
        }
    }

    var shouldRender: Bool {
        #if os(iOS)
        placement == .menu
        #else
        true
        #endif
    }
}
```

In the above example, search suggestions only render in iOS if the searchable modifier displays them in a menu. You might want to do this to render suggestions in your own list alongside your own search results when they would render in a list.

## See Also

- [var buttonRepeatBehavior: ButtonRepeatBehavior](environmentvalues/buttonrepeatbehavior.md)
  Whether buttons with this associated environment should repeatedly trigger their actions on prolonged interactions.
- [var defaultWheelPickerItemHeight: CGFloat](environmentvalues/defaultwheelpickeritemheight.md)
  The default height of an item in a wheel-style picker, such as a date picker.
- [var keyboardShortcut: KeyboardShortcut?](environmentvalues/keyboardshortcut.md)
  The keyboard shortcut that buttons in this environment will be triggered with.
- [var menuIndicatorVisibility: Visibility](environmentvalues/menuindicatorvisibility.md)
  The menu indicator visibility to apply to controls within a view.
- [var menuOrder: MenuOrder](environmentvalues/menuorder.md)
  The preferred order of items for menus presented from this view.
- [var preferredPencilDoubleTapAction: PencilPreferredAction](environmentvalues/preferredpencildoubletapaction.md)
  The action that the user prefers to perform after double-tapping their Apple Pencil, as selected in the Settings app.
- [var preferredPencilSqueezeAction: PencilPreferredAction](environmentvalues/preferredpencilsqueezeaction.md)
  The action that the user prefers to perform when squeezing their Apple Pencil, as selected in the Settings app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/searchsuggestionsplacement)*