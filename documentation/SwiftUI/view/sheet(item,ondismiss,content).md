# sheet(item:onDismiss:content:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents a sheet using the given item as a data source for the sheet’s content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)? = nil, @ContentBuilder content: @escaping (Item) -> Content) -> some View where Item : Identifiable, Content : View
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

![A view showing a custom structure acting as a data source, providing](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-View-SheetItemContent@2x.png)

In vertically compact environments, such as iPhone in landscape orientation, a sheet presentation automatically adapts to appear as a full-screen cover. Use the [`presentationCompactAdaptation(_:)`](./presentationcompactadaptation%28_%29.md) or [`presentationCompactAdaptation(horizontal:vertical:)`](./presentationcompactadaptation%28horizontal,vertical%29.md) modifier to override this behavior.

##### Breakthrough effect

In visionOS, most system presentations appear with a breakthrough effect by default. To change how the enclosing presentation breaks through content occluding it, use [`presentationBreakthroughEffect(_:)`](./presentationbreakthrougheffect%28_%29.md), like in the following example:

```swift
.sheet(item: $sheetDetail,
       onDismiss: didDismiss) { detail in
    VStack(alignment: .leading, spacing: 20) {
        Text("Part Number: \(detail.partNumber)")
        Text("Name: \(detail.name)")
        Text("Quantity On-Hand: \(detail.quantity)")
    }
    .presentationBreakthroughEffect(.prominent)
    .onTapGesture {
        sheetDetail = nil
    }
}
```

> **Note**: Passing a `.none` value for a sheet has no effect.

## Parameters

- `item`: A binding to an optional source of truth for the sheet. When `item` is non-`nil`, the system passes the item’s content to the modifier’s closure. You display this content in a sheet that you create that the system displays to the user. If `item` changes, the system dismisses the sheet and replaces it with a new one using the same process.
- `onDismiss`: The closure to execute when dismissing the sheet.
- `content`: A closure returning the content of the sheet.

## See Also

### Showing a sheet, cover, or popover
- [func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?, content: () -> Content) -> some View](./sheet%28ispresented,ondismiss,content%29.md)
  Presents a sheet when a binding to a Boolean value that you provide is true.
- [func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?, content: () -> Content) -> some View](./fullscreencover%28ispresented,ondismiss,content%29.md)
  Presents a modal view that covers as much of the screen as possible when binding to a Boolean value you provide is true.
- [func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?, content: (Item) -> Content) -> some View](./fullscreencover%28item,ondismiss,content%29.md)
  Presents a modal view that covers as much of the screen as possible using the binding you provide as a data source for the sheet’s content.
- [func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: (Item) -> Content) -> some View](./popover%28item,attachmentanchor,arrowedge,content%29.md)
  Presents a popover using the given item as a data source for the popover’s content.
- [func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: () -> Content) -> some View](./popover%28ispresented,attachmentanchor,arrowedge,content%29.md)
  Presents a popover when a given condition is true.
- [enum PopoverAttachmentAnchor](../popoverattachmentanchor.md)
  An attachment anchor for a popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/sheet(item:ondismiss:content:))*