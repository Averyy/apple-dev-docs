# alert(isPresented:content:)

**Framework**: SwiftUI  
**Kind**: method

Presents an alert to the user.

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
func alert(isPresented: Binding<Bool>, content: () -> Alert) -> some View
```

#### Discussion

Use this method when you need to show an alert to the user. The example below displays an alert that is shown when the user toggles a Boolean value that controls the presentation of the alert:

```swift
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

![An alert whose title reads Order Complete, with the message, Thank you for shopping with us placed underneath. The alert also includes an OK button for dismissing the alert.](https://docs-assets.developer.apple.com/published/484648a41f7dabaa507054457b090206/SwiftUI-View-AlertIsPresentedContent%402x.png)

## Parameters

- `isPresented`: A binding to a Boolean value that determines whether   to present the alert that you create in the modifier’s   closure. When the   user presses or taps OK the system sets   to    which dismisses the alert.
- `content`: A closure returning the alert to present.

## See Also

- [func actionSheet(isPresented: Binding<Bool>, content: () -> ActionSheet) -> some View](view/actionsheet(ispresented:content:).md)
  Presents an action sheet when a given condition is true.
- [func actionSheet<T>(item: Binding<T?>, content: (T) -> ActionSheet) -> some View](view/actionsheet(item:content:).md)
  Presents an action sheet using the given item as a data source for the sheet’s content.
- [func alert<Item>(item: Binding<Item?>, content: (Item) -> Alert) -> some View](view/alert(item:content:).md)
  Presents an alert to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/alert(ispresented:content:))*