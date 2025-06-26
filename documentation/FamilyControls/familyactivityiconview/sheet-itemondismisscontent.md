# sheet(item:onDismiss:content:)

**Framework**: FamilyControls  
**Kind**: method

Presents a sheet using the given item as a data source for the sheet’s content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)? = nil, @ViewBuilder content: @escaping (Item) -> Content) -> some View where Item : Identifiable, Content : View
```

#### Discussion

Use this method when you need to present a modal view with content from a custom data source. The example below shows a custom data source `InventoryItem` that the `content` closure uses to populate the display the action sheet shows to the user:

```swift
struct ShowPartDetail: View {
    @State private var sheetDetail: InventoryItem?

    var body: some View {
        Button("Show Part Details") {
            sheetDetail = InventoryItem(
                id: "0123456789",
                partNumber: "Z-1234A",
                quantity: 100,
                name: "Widget")
        }
        .sheet(item: $sheetDetail,
               onDismiss: didDismiss) { detail in
            VStack(alignment: .leading, spacing: 20) {
                Text("Part Number: \(detail.partNumber)")
                Text("Name: \(detail.name)")
                Text("Quantity On-Hand: \(detail.quantity)")
            }
            .onTapGesture {
                sheetDetail = nil
            }
        }
    }

    func didDismiss() {
        // Handle the dismissing action.
    }
}

struct InventoryItem: Identifiable {
    var id: String
    let partNumber: String
    let quantity: Int
    let name: String
}
```

In vertically compact environments, such as iPhone in landscape orientation, a sheet presentation automatically adapts to appear as a full-screen cover. Use the `View/presentationCompactAdaptation(_:)` or `View/presentationCompactAdaptation(horizontal:vertical:)` modifier to override this behavior.

## Parameters

- `item`: A binding to an optional source of truth for the sheet.   When   is non- , the system passes the item’s content to   the modifier’s closure. You display this content in a sheet that you   create that the system displays to the user. If   changes,   the system dismisses the sheet and replaces it with a new one   using the same process.
- `onDismiss`: The closure to execute when dismissing the sheet.
- `content`: A closure returning the content of the sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/sheet(item:ondismiss:content:))*