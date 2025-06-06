# actionSheet(isPresented:content:)

**Framework**: Journalingsuggestions  
**Kind**: method

Presents an action sheet when a given condition is true.

**Availability**:
- iOS 13.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func actionSheet(isPresented: Binding<Bool>, content: () -> ActionSheet) -> some View
```

#### Discussion

In the example below, a button conditionally presents an action sheet depending upon the value of a bound Boolean variable. When the Boolean value is set to `true`, the system displays an action sheet with both destructive and default actions:

```None
struct ConfirmEraseItems: View {
    @State private var isShowingSheet = false
    var body: some View {
        Button("Show Action Sheet", action: {
            isShowingSheet = true
        })
        .actionSheet(isPresented: $isShowingSheet) {
            ActionSheet(
                title: Text("Permanently erase the items in the Trash?"),
                message: Text("You can't undo this action."),
                buttons:[
                    .destructive(Text("Empty Trash"),
                                 action: emptyTrashAction),
                    .cancel()
                ]
            )}
    }

    func emptyTrashAction() {
        // Handle empty trash action.
    }
}
```

> **Note**: In regular size classes in iOS, the system renders alert sheets as a popover that the user dismisses by tapping anywhere outside the popover, rather than displaying the default dismiss button.

## Parameters

- `isPresented`: A binding to a Boolean value that determines whether   to present the action sheet that you create in the modifier’s    closure. When the user presses or taps the sheet’s default   action button the system sets this value to   dismissing   the sheet.
- `content`: A closure returning the   to present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/actionsheet(ispresented:content:))*