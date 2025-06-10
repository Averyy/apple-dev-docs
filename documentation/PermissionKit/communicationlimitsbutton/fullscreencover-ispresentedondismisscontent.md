# fullScreenCover(isPresented:onDismiss:content:)

**Framework**: PermissionKit  
**Kind**: method

Presents a modal view that covers as much of the screen as possible when binding to a Boolean value you provide is true.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 26.0+ (Beta)
- watchOS 7.0+

## Declaration

```swift
nonisolated
func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)? = nil, @ViewBuilder content: @escaping () -> Content) -> some View where Content : View
```

#### Discussion

Use this method to show a modal view that covers as much of the screen as possible. The example below displays a custom view when the user toggles the value of the `isPresenting` binding:

```None
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/fullscreencover(ispresented:ondismiss:content:))*