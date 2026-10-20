# sheet(isPresented:onDismiss:content:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents a sheet when a binding to a Boolean value that you provide is true.

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
func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)? = nil, @ContentBuilder content: @escaping () -> Content) -> some View where Content : View
```

#### Discussion

Use this method when you want to present a modal view to the user when a Boolean value you provide is true. The example below displays a modal view of the mockup for a software license agreement when the user toggles the `isShowingSheet` variable by clicking or tapping on the “Show License Agreement” button:

```swift
struct ShowLicenseAgreement: View {
    @State private var isShowingSheet = false
    var body: some View {
        Button(action: {
            isShowingSheet.toggle()
        }) {
            Text("Show License Agreement")
        }
        .sheet(isPresented: $isShowingSheet,
               onDismiss: didDismiss) {
            VStack {
                Text("License Agreement")
                    .font(.title)
                    .padding(50)
                Text("""
                        Terms and conditions go here.
                    """)
                    .padding(50)
                Button("Dismiss",
                       action: { isShowingSheet.toggle() })
            }
        }
    }

    func didDismiss() {
        // Handle the dismissing action.
    }
}
```

![A screenshot of a full-screen modal sheet showing the mockup of a](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-View-SheetIsPresentingContent@2x.png)

In vertically compact environments, such as iPhone in landscape orientation, a sheet presentation automatically adapts to appear as a full-screen cover. Use the [`presentationCompactAdaptation(_:)`](./presentationcompactadaptation%28_%29.md) or [`presentationCompactAdaptation(horizontal:vertical:)`](./presentationcompactadaptation%28horizontal,vertical%29.md) modifier to override this behavior.

##### Breakthrough effect

In visionOS, most system presentations appear with a breakthrough effect by default. To change how the enclosing presentation breaks through content occluding it, use [`presentationBreakthroughEffect(_:)`](./presentationbreakthrougheffect%28_%29.md), like in the following example:

```swift
.sheet(isPresented: $isShowingSheet,
       onDismiss: didDismiss) {
    VStack {
        Text("License Agreement")
            .font(.title)
            .padding(50)
        Text("""
                Terms and conditions go here.
            """)
            .padding(50)
        Button("Dismiss",
               action: { isShowingSheet.toggle() })
    }
    .presentationBreakthroughEffect(.prominent)
}
```

> **Note**: Passing a `.none` value for a sheet has no effect.

## Parameters

- `isPresented`: A binding to a Boolean value that determines whether to present the sheet that you create in the modifier’s `content` closure.
- `onDismiss`: The closure to execute when dismissing the sheet.
- `content`: A closure that returns the content of the sheet.

## See Also

### Showing a sheet, cover, or popover
- [func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?, content: (Item) -> Content) -> some View](./sheet%28item,ondismiss,content%29.md)
  Presents a sheet using the given item as a data source for the sheet’s content.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/sheet(ispresented:ondismiss:content:))*