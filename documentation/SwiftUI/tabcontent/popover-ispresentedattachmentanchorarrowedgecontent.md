# popover(isPresented:attachmentAnchor:arrowEdge:content:)

**Framework**: SwiftUI  
**Kind**: method

Presents a popover when a given condition is true.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor: PopoverAttachmentAnchor = .rect(.bounds), arrowEdge: Edge? = nil, @ViewBuilder content: @escaping () -> Content) -> some TabContent<Self.TabValue> where Content : View
```

#### Discussion

Use this method to show a popover whose contents are a SwiftUI view that you provide when a bound Boolean variable is `true`. In the example below, a popover displays whenever the user toggles the `isShowingPopover` state variable by pressing the “Show Popover” button:

```swift
struct PopoverExample: View {
    @State private var isShowingPopover = false

    var body: some View {
        TabView {
            Tab("Popover Anchor", systemImage: "arrow.down") {
                Button("Show Popover") {
                    self.isShowingPopover = true
                }
            }
            .popover(isPresented: $isShowingPopover) {
                Text("Popover Content")
                    .padding()
            }
        }
    }
}
```

## Parameters

- `isPresented`: A binding to a Boolean value that determines whether   to present the popover content that you return from the modifier’s    closure.
- `attachmentAnchor`: The positioning anchor that defines the   attachment point of the popover. The default is   .
- `arrowEdge`: The edge of the   that defines the   location of the popover’s arrow in macOS. The default is  .
- `content`: A closure returning the content of the popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabcontent/popover(ispresented:attachmentanchor:arrowedge:content:))*