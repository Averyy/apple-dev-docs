# fullScreenCover(isPresented:onDismiss:content:)

**Framework**: FamilyControls  
**Kind**: method

Presents a modal view that covers as much of the screen as possible when binding to a Boolean value you provide is true.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- tvOS 14.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)? = nil, @ViewBuilder content: @escaping () -> Content) -> some View where Content : View
```

#### Discussion

Use this method to show a modal view that covers as much of the screen as possible. The example below displays a custom view when the user toggles the value of the `isPresenting` binding:

```swift
struct FullScreenCoverPresentedOnDismiss: View {
    @State private var isPresenting = false
    var body: some View {
        Button("Present Full-Screen Cover") {
            isPresenting.toggle()
        }
        .fullScreenCover(isPresented: $isPresenting,
                         onDismiss: didDismiss) {
            VStack {
                Text("A full-screen modal view.")
                    .font(.title)
                Text("Tap to Dismiss")
            }
            .onTapGesture {
                isPresenting.toggle()
            }
            .foregroundColor(.white)
            .frame(maxWidth: .infinity,
                   maxHeight: .infinity)
            .background(Color.blue)
            .ignoresSafeArea(edges: .all)
        }
    }

    func didDismiss() {
        // Handle the dismissing action.
    }
}
```

## Parameters

- `isPresented`: A binding to a Boolean value that determines whether   to present the sheet.
- `onDismiss`: The closure to execute when dismissing the modal view.
- `content`: A closure that returns the content of the modal view.

## See Also

- [func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?, content: () -> Content) -> some View](familyactivitypicker/sheet(ispresented:ondismiss:content:).md)
  Presents a sheet when a binding to a Boolean value that you provide is true.
- [func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?, content: (Item) -> Content) -> some View](familyactivitypicker/sheet(item:ondismiss:content:).md)
  Presents a sheet using the given item as a data source for the sheet’s content.
- [func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?, content: (Item) -> Content) -> some View](familyactivitypicker/fullscreencover(item:ondismiss:content:).md)
  Presents a modal view that covers as much of the screen as possible using the binding you provide as a data source for the sheet’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/fullscreencover(ispresented:ondismiss:content:))*