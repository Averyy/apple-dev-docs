# popover(item:attachmentAnchor:arrowEdge:content:)

**Framework**: FinanceKitUI  
**Kind**: method

Presents a popover using the given item as a data source for the popover’s content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
nonisolated
func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor: PopoverAttachmentAnchor = .rect(.bounds), arrowEdge: Edge? = nil, @ViewBuilder content: @escaping (Item) -> Content) -> some View where Item : Identifiable, Content : View
```

#### Discussion

Use this method when you need to present a popover with content from a custom data source. The example below uses data in the `PopoverModel` structure to populate the view in the `content` closure that the popover displays to the user:

```None
struct PopoverExample: View {
    @State private var popover: PopoverModel?

    var body: some View {
        Button("Show Popover") {
            popover = PopoverModel(message: "Custom Message")
        }
        .popover(item: $popover, arrowEdge: .bottom) { detail in
            Text("\(detail.message)")
                .padding()
        }
    }
}

struct PopoverModel: Identifiable {
    var id: String { message }
    let message: String
}
```

> ❗ **Important**: Prior to iOS 18.1, the popover arrow edge was not respected. Apps that are re-compiled with the iOS 18.1 or later SDK or visionOS 2.1 or later SDK and run on iOS 18.1 or later or visionOS 2.1 or later have the arrow edge respected. On macOS, arrow edge has always been respected. Alternatively, to allow the system to choose the best orientation of the popover’s arrow, use the `View/popover(item:attachmentAnchor:content:)` variant.

Prior to iOS 18.1, the popover arrow edge was not respected. Apps that are re-compiled with the iOS 18.1 or later SDK or visionOS 2.1 or later SDK and run on iOS 18.1 or later or visionOS 2.1 or later have the arrow edge respected. On macOS, arrow edge has always been respected. Alternatively, to allow the system to choose the best orientation of the popover’s arrow, use the `View/popover(item:attachmentAnchor:content:)` variant.

## Parameters

- `item`: A binding to an optional source of truth for the popover.   When   is non- , the system passes the contents to   the modifier’s closure. You use this content to populate the fields   of a popover that you create that the system displays to the user.   If   changes, the system dismisses the currently presented   popover and replaces it with a new popover using the same process.
- `attachmentAnchor`: The positioning anchor that defines the   attachment point of the popover. The default is   .
- `arrowEdge`: The edge of the   that defines the   location of the popover’s arrow. The default is   , which results in the system allowing any arrow edge.
- `content`: A closure returning the content of the popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/addordertowalletbutton/popover(item:attachmentanchor:arrowedge:content:))*