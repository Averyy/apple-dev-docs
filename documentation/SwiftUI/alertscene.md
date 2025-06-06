# AlertScene

**Framework**: SwiftUI  
**Kind**: struct

A scene that renders itself as a standalone alert dialog.

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct AlertScene<Actions, Message> where Actions : View, Message : View
```

#### Overview

Alert scenes are not attached to any particular window, and present themselves in the center of the current display. The dialog must be dismissed before any further interaction with the app is permitted.

```swift
@main
struct MyApp: App {
    @State var showLoginAlert = true
    @State var loggedIn = false

    var body: some Scene {
        Window("Welcome User Window", id:"WelcomeWindow") {
            ...
        }
        .defaultLaunchBehavior(loggedIn ? .presented : .suppressed)

        AlertScene("Login Required", isPresented: $showLoginAlert) {
            Button("OK") {
                ...
            }
        }
    }
}
```

All actions present in the ViewBuilder will dismiss the alert. Like the alert modifier, you can determine the role of the buttons with `.cancel` or `.destructive`. If no actions are present, we will automatically include an OK button for dismissal.

## Topics

### Initializers
- [init(_:isPresented:actions:)](alertscene/init(_:ispresented:actions:).md)
  Creates an alert scene with a title and a set of actions.
- [init(_:isPresented:actions:message:)](alertscene/init(_:ispresented:actions:message:).md)
  Creates an alert scene with a title, a set of actions, and a message.
- [init(_:isPresented:presenting:actions:)](alertscene/init(_:ispresented:presenting:actions:).md)
  Creates an alert scene, using the given data to produce the alert’s content with a title, and a set of actions. Note that this creates a text view on your behalf.
- [init(_:isPresented:presenting:actions:message:)](alertscene/init(_:ispresented:presenting:actions:message:).md)
  Creates an alert scene, using the given data to produce the alert’s content with a title, a set of actions, and a message. Note that this creates a text view on your behalf.

## Relationships

### Conforms To
- [Scene](scene.md)

## See Also

- [func alert(_:isPresented:actions:)](view/alert(_:ispresented:actions:).md)
  Presents an alert when a given condition is true, using a text view for the title.
- [func alert(_:isPresented:presenting:actions:)](view/alert(_:ispresented:presenting:actions:).md)
  Presents an alert using the given data to produce the alert’s content and a text view as a title.
- [func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) -> some View](view/alert(ispresented:error:actions:).md)
  Presents an alert when an error is present.
- [func alert(_:isPresented:actions:message:)](view/alert(_:ispresented:actions:message:).md)
  Presents an alert with a message when a given condition is true using a text view as a title.
- [func alert(_:isPresented:presenting:actions:message:)](view/alert(_:ispresented:presenting:actions:message:).md)
  Presents an alert with a message using the given data to produce the alert’s content and a text view for a title.
- [func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A, message: (E) -> M) -> some View](view/alert(ispresented:error:actions:message:).md)
  Presents an alert with a message when an error is present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/alertscene)*