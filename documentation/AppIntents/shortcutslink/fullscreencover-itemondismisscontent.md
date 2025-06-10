# fullScreenCover(item:onDismiss:content:)

**Framework**: App Intents  
**Kind**: method

Presents a modal view that covers as much of the screen as possible using the binding you provide as a data source for the sheet’s content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)? = nil, @ViewBuilder content: @escaping (Item) -> Content) -> some View where Item : Identifiable, Content : View
```

#### Discussion

Use this method to display a modal view that covers as much of the screen as possible. In the example below a custom structure — `CoverData` — provides data for the full-screen view to display in the `content` closure when the user clicks or taps the “Present Full-Screen Cover With Data” button:

```swift
struct FullScreenCoverItemOnDismissContent: View {
    @State private var coverData: CoverData?

    var body: some View {
        Button("Present Full-Screen Cover With Data") {
            coverData = CoverData(body: "Custom Data")
        }
        .fullScreenCover(item: $coverData,
                         onDismiss: didDismiss) { details in
            VStack(spacing: 20) {
                Text("\(details.body)")
            }
            .onTapGesture {
                coverData = nil
            }
        }
    }

    func didDismiss() {
        // Handle the dismissing action.
    }

}

struct CoverData: Identifiable {
    var id: String {
        return body
    }
    let body: String
}
```

## Parameters

- `item`: A binding to an optional source of truth for the sheet.   When   is non- , the system passes the contents to   the modifier’s closure. You display this content in a sheet that you   create that the system displays to the user. If   changes,   the system dismisses the currently displayed sheet and replaces   it with a new one using the same process.
- `onDismiss`: The closure to execute when dismissing the modal view.
- `content`: A closure returning the content of the modal view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/fullscreencover(item:ondismiss:content:))*