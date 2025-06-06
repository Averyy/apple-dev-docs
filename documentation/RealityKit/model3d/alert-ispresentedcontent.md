# alert(isPresented:content:)

**Framework**: RealityKit  
**Kind**: method

Presents an alert to the user.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func alert(isPresented: Binding<Bool>, content: () -> Alert) -> some View
```

#### Discussion

Use this method when you need to show an alert to the user. The example below displays an alert that is shown when the user toggles a Boolean value that controls the presentation of the alert:

```None
struct OrderCompleteAlert: View {
    @State private var isPresented = false
    var body: some View {
        Button("Show Alert", action: {
            isPresented = true
        })
        .alert(isPresented: $isPresented) {
            Alert(title: Text("Order Complete"),
                  message: Text("Thank you for shopping with us."),
                  dismissButton: .default(Text("OK")))
        }
    }
}
```

## Parameters

- `isPresented`: A binding to a Boolean value that determines whether   to present the alert that you create in the modifier’s   closure. When the   user presses or taps OK the system sets   to    which dismisses the alert.
- `content`: A closure returning the alert to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3d/alert(ispresented:content:))*