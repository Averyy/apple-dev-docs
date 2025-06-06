# Window

**Framework**: Swiftui  
**Kind**: struct

A scene that presents its content in a single, unique window.

**Availability**:
- macOS 13.0+

## Declaration

```swift
struct Window<Content> where Content : View
```

#### Overview

Use a `Window` scene to augment the main interface of your app with a window that gives people access to supplemental functionality. For example, you can create a secondary window in a mail reader app that enables people to view the status of their account connections:

```swift
 @main
 struct Mail: App {
     var body: some Scene {
         WindowGroup {
             MailViewer()
         }
         Window("Connection Doctor", id: "connection-doctor") {
             ConnectionDoctor()
         }
     }
 }
```

Provide a title as the first argument to the window’s intializer. The system uses the title to identify the window to people using your app in the window’s title bar or in the list of available singleton windows that the Windows menu displays automatically.

> **Note**: You can override the title in the window’s title bar by adding one of the [`navigationTitle(_:)`](view/navigationtitle(_:).md) view modifiers to the window’s content. This enables you to dynamically update the title bar.

##### Open a Window Programmatically

People open the window by selecting it in the Windows menu, but you can also open the window programmatically using the [`openWindow`](environmentvalues/openwindow.md) action that you read from the environment. Use the `id` parameter that you initialize the window with to indicate which window to open. For example, you can create a button to open the window from the previous example:

```swift
struct OpenConnectionDoctorButton: View {
    @Environment(\.openWindow) private var openWindow

    var body: some View {
        Button("Connection doctor") {
            openWindow(id: "connection-doctor") // Match the window's identifier.
        }
    }
}
```

If the window is already open when you call this action, the action brings the open window to the front. Be sure to use unique identifiers across all of the `Window` and [`WindowGroup`](windowgroup.md) instances that you define.

##### Dismiss a Window Programmatically

The system provides people with controls to close windows, but you can also close a window programmatically using the [`dismiss`](environmentvalues/dismiss.md) action from within the window’s view hierarchy. For example, you can include a button in the connection doctor view that dismisses the view:

```swift
struct ConnectionDoctor: View {
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        VStack {
            // ...

            Button("Dismiss") {
                dismiss()
            }
        }
    }
}
```

The dismiss action doesn’t close the window if you call it from a modal — like a sheet or a popover — that you present from within the window. In that case, the action dismisses the modal presentation instead.

##### Use a Window As the Main Scene

You can use a window as the main scene of your app when multi-window functionality isn’t appropriate. For example, it might not make sense to display more than one window for a video call app that relies on a hardware resource, like a camera:

```swift
@main
struct VideoCall: App {
    var body: some Scene {
        Window("VideoCall", id: "main") {
            CameraView()
        }
    }
}
```

If your app uses a single window as its primary scene, the app quits when the window closes. This behavior differs from an app that uses a [`WindowGroup`](windowgroup.md) as its primary scene, where the app continues to run even after closing all of its windows.

> **Note**: In most cases it’s best to use a [`WindowGroup`](windowgroup.md) to represent the main scene of your app. A window group provides multi-window functionality on platforms that support it, like iPadOS and macOS, and makes it easier to share code across platforms.

## Topics

### Creating a window
- [init(_:id:content:)](window/init(_:id:content:).md)
  Creates a window with a title and an identifier.

## Relationships

### Conforms To
- [Scene](scene.md)

## See Also

- [struct WindowGroup](windowgroup.md)
  A scene that presents a group of identically structured windows.
- [struct UtilityWindow](utilitywindow.md)
  A specialized window scene that provides secondary utility to the content of the main scenes of an application.
- [protocol WindowStyle](windowstyle.md)
  A specification for the appearance and interaction of a window.
- [func windowStyle<S>(S) -> some Scene](scene/windowstyle(_:).md)
  Sets the style for windows created by this scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SwiftUI/window)*