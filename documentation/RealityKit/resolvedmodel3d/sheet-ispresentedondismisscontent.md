# sheet(isPresented:onDismiss:content:)

**Framework**: RealityKit  
**Kind**: method

Presents a sheet when a binding to a Boolean value that you provide is true.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)? = nil, @ViewBuilder content: @escaping () -> Content) -> some View where Content : View
```

#### Discussion

Use this method when you want to present a modal view to the user when a Boolean value you provide is true. The example below displays a modal view of the mockup for a software license agreement when the user toggles the `isShowingSheet` variable by clicking or tapping on the “Show License Agreement” button:

```None
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

In vertically compact environments, such as iPhone in landscape orientation, a sheet presentation automatically adapts to appear as a full-screen cover. Use the `View/presentationCompactAdaptation(_:)` or `View/presentationCompactAdaptation(horizontal:vertical:)` modifier to override this behavior.

## Parameters

- `isPresented`: A binding to a Boolean value that determines whether   to present the sheet that you create in the modifier’s    closure.
- `onDismiss`: The closure to execute when dismissing the sheet.
- `content`: A closure that returns the content of the sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/resolvedmodel3d/sheet(ispresented:ondismiss:content:))*