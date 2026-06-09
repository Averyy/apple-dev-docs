# keyboard

**Framework**: SwiftUI  
**Kind**: property

A placement for items in the keyboard section.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
static let keyboard: ToolbarItemPlacement
```

#### Discussion

On iOS, keyboard items are above the software keyboard when present, or at the bottom of the screen when a hardware keyboard is attached.

On macOS, keyboard items will be placed inside the Touch Bar.

A `FocusedValue` can be used to adjust the content of the keyboard bar based on the currently focused view. In the example below, the keyboard bar gains additional buttons only when the appropriate `TextField` is focused.

```swift
enum Field {
    case suit
    case rank
}

struct KeyboardBarDemo : View {
    @FocusedValue(\.field) var field: Field?

    var body: some View {
        HStack {
            TextField("Suit", text: $suitText)
                .focusedValue(\.field, .suit)
            TextField("Rank", text: $rankText)
                .focusedValue(\.field, .rank)
        }
        .toolbar {
            ToolbarItemGroup(placement: .keyboard) {
                if field == .suit {
                    Button("♣️", action: {})
                    Button("♥️", action: {})
                    Button("♠️", action: {})
                    Button("♦️", action: {})
                }
                DoneButton()
            }
        }
    }
}
```

## See Also

- [static var topBarLeading: ToolbarItemPlacement](toolbaritemplacement/topbarleading.md)
  A placement for items in the leading edge of the top bar.
- [static var topBarTrailing: ToolbarItemPlacement](toolbaritemplacement/topbartrailing.md)
  A placement for items in the trailing edge of the top bar.
- [static let topBarPinnedTrailing: ToolbarItemPlacement](toolbaritemplacement/topbarpinnedtrailing.md)
  A placement that pins the item to the trailing edge of the toolbar.
- [static let bottomBar: ToolbarItemPlacement](toolbaritemplacement/bottombar.md)
  A placement for items in the bottom toolbar.
- [static let bottomOrnament: ToolbarItemPlacement](toolbaritemplacement/bottomornament.md)
  A placement for items in an ornament under the window.
- [static func accessoryBar<ID>(id: ID) -> ToolbarItemPlacement](toolbaritemplacement/accessorybar(id:).md)
  Creates a unique accessory bar placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/keyboard)*