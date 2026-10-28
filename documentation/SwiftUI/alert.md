# Alert

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A representation of an alert presentation.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 10.15+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use a [`View`](./view.md) modifier like [`alert(_:isPresented:presenting:actions:message:)`](./view/alert%28_,ispresented,presenting,actions,message%29-8584l.md) instead.

## Declaration

```swift
struct Alert
```

## Overview

Use an alert when you want the user to act in response to the state of the app or system. If you want the user to make a choice in response to their action, use an [`ActionSheet`](./actionsheet.md) instead.

You show an alert by using the [`alert(isPresented:content:)`](./view/alert%28ispresented,content%29.md) view modifier to create an alert, which then appears whenever the bound `isPresented` value is `true`. The `content` closure you provide to this modifer produces a customized instance of the `Alert` type.

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

![A default alert dialog with the title Current Location Not Available in bold text, the message your current location can’t be determined at this time in smaller text, and a default OK button.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-Alert-OK@2x.png)

To customize the alert, add instances of the [`Alert.Button`](./alert/button.md) type, which provides standardized buttons for common tasks like canceling and performing destructive actions. The following example uses two buttons: a default button labeled “Try Again” that calls a `saveWorkoutData` method, and a “Delete” button that calls a destructive `deleteWorkoutData` method.

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

![An alert dialog with the title, Unable to Save Workout Data in bold text, and](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-Alert-default-and-destructive@2x.png)

The alert handles its own dismissal when the user taps one of the buttons in the alert, by setting the bound `isPresented` value back to `false`.

## Topics

### Creating an alert
- [init(title: Text, message: Text?, dismissButton: Alert.Button?)](./alert/init%28title,message,dismissbutton%29.md)
  Creates an alert with one button.
- [init(title: Text, message: Text?, primaryButton: Alert.Button, secondaryButton: Alert.Button)](./alert/init%28title,message,primarybutton,secondarybutton%29.md)
  Creates an alert with two buttons.
- [static func sideBySideButtons(title: Text, message: Text?, primaryButton: Alert.Button, secondaryButton: Alert.Button) -> Alert](./alert/sidebysidebuttons%28title,message,primarybutton,secondarybutton%29.md)
  Creates a side by side button alert.
### Specifying the button type
- [struct Button](./alert/button.md)
  A button that represents an operation of an alert presentation.

## See Also

### Deprecated
- [struct ActionSheet](./actionsheet.md)
  A representation of an action sheet presentation.
- [func fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)](./view/fileexporter%28ispresented,document,contenttype,defaultfilename,oncompletion%29.md)
  Presents a system dialog for exporting a document that’s stored in a value type, like a structure, to a file on disk.
- [func fileExporter(isPresented:documents:contentType:onCompletion:)](./view/fileexporter%28ispresented,documents,contenttype,oncompletion%29.md)
  Presents a system dialog for exporting a collection of value type documents to files on disk.
- [func fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)](./view/fileexporter%28ispresented,document,contenttypes,defaultfilename,oncompletion,oncancellation%29.md)
  Presents a system dialog for allowing the user to export a `FileDocument` to a file on disk.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alert)*