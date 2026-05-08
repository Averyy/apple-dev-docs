# Alert

**Framework**: SwiftUI  
**Kind**: struct

A representation of an alert presentation.

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
struct Alert
```

#### Overview

Use an alert when you want the user to act in response to the state of the app or system. If you want the user to make a choice in response to their action, use an [`ActionSheet`](actionsheet.md) instead.

You show an alert by using the [`alert(isPresented:content:)`](view/alert(ispresented:content:).md) view modifier to create an alert, which then appears whenever the bound `isPresented` value is `true`. The `content` closure you provide to this modifer produces a customized instance of the `Alert` type.

In the following example, a button presents a simple alert when tapped, by updating a local `showAlert` property that binds to the alert.

```swift
@State private var showAlert = false
var body: some View {
    Button("Tap to show alert") {
        showAlert = true
    }
    .alert(isPresented: $showAlert) {
        Alert(
            title: Text("Current Location Not Available"),
            message: Text("Your current location can’t be " +
                            "determined at this time.")
        )
    }
}
```

![A default alert dialog with the title Current Location Not Available in bold text, the message your current location can’t be determined at this time in smaller text, and a default OK button.](https://docs-assets.developer.apple.com/published/8ebf34ed1e8f5e8b85930f7576e9371e/SwiftUI-Alert-OK%402x.png)

To customize the alert, add instances of the [`Alert.Button`](alert/button.md) type, which provides standardized buttons for common tasks like canceling and performing destructive actions. The following example uses two buttons: a default button labeled “Try Again” that calls a `saveWorkoutData` method, and a “Delete” button that calls a destructive `deleteWorkoutData` method.

```swift
@State private var showAlert = false
var body: some View {
    Button("Tap to show alert") {
        showAlert = true
    }
    .alert(isPresented: $showAlert) {
        Alert(
            title: Text("Unable to Save Workout Data"),
            message: Text("The connection to the server was lost."),
            primaryButton: .default(
                Text("Try Again"),
                action: saveWorkoutData
            ),
            secondaryButton: .destructive(
                Text("Delete"),
                action: deleteWorkoutData
            )
        )
    }
}
```

![An alert dialog with the title, Unable to Save Workout Data in bold text, and](https://docs-assets.developer.apple.com/published/b0cc30235176ee89cfb5db5aebe43368/SwiftUI-Alert-default-and-destructive%402x.png)

The alert handles its own dismissal when the user taps one of the buttons in the alert, by setting the bound `isPresented` value back to `false`.

## Topics

### Creating an alert
- [init(title: Text, message: Text?, dismissButton: Alert.Button?)](alert/init(title:message:dismissbutton:).md)
  Creates an alert with one button.
- [init(title: Text, message: Text?, primaryButton: Alert.Button, secondaryButton: Alert.Button)](alert/init(title:message:primarybutton:secondarybutton:).md)
  Creates an alert with two buttons.
- [static func sideBySideButtons(title: Text, message: Text?, primaryButton: Alert.Button, secondaryButton: Alert.Button) -> Alert](alert/sidebysidebuttons(title:message:primarybutton:secondarybutton:).md)
  Creates a side by side button alert.
### Specifying the button type
- [struct Button](alert/button.md)
  A button that represents an operation of an alert presentation.

## See Also

- [struct ActionSheet](actionsheet.md)
  A representation of an action sheet presentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alert)*