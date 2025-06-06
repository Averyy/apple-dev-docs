# System events

**Framework**: SwiftUI

React to system events, like opening a URL.

#### Overview

Specify view and scene modifiers to indicate how your app responds to certain system events. For example, you can use the [`onOpenURL(perform:)`](view/onopenurl(perform:).md) view modifier to define an action to take when your app receives a universal link, or use the [`backgroundTask(_:action:)`](scene/backgroundtask(_:action:).md) scene modifier to specify an asynchronous task to carry out in response to a background task event, like the completion of a background URL session.

![None](https://docs-assets.developer.apple.com/published/b70766bbbd9cc1bd02c1faddc9c01a4e/system-events-hero%402x.png)

## Topics

### Sending and receiving user activities
- [Restoring Your App’s State with SwiftUI](restoring_your_app_s_state_with_swiftui.md)
  Provide app continuity for users by preserving their current activities.
- [func userActivity<P>(String, element: P?, (P, NSUserActivity) -> ()) -> some View](view/useractivity(_:element:_:).md)
  Advertises a user activity type.
- [func userActivity(String, isActive: Bool, (NSUserActivity) -> ()) -> some View](view/useractivity(_:isactive:_:).md)
  Advertises a user activity type.
- [func onContinueUserActivity(String, perform: (NSUserActivity) -> ()) -> some View](view/oncontinueuseractivity(_:perform:).md)
  Registers a handler to invoke in response to a user activity that your app receives.
### Sending and receiving URLs
- [var openURL: OpenURLAction](environmentvalues/openurl.md)
  An action that opens a URL.
- [struct OpenURLAction](openurlaction.md)
  An action that opens a URL.
- [func onOpenURL(perform: (URL) -> ()) -> some View](view/onopenurl(perform:).md)
  Registers a handler to invoke in response to a URL that your app receives.
### Handling external events
- [func handlesExternalEvents(matching: Set<String>) -> some Scene](scene/handlesexternalevents(matching:).md)
  Specifies the external events for which SwiftUI opens a new instance of the modified scene.
- [func handlesExternalEvents(preferring: Set<String>, allowing: Set<String>) -> some View](view/handlesexternalevents(preferring:allowing:).md)
  Specifies the external events that the view’s scene handles if the scene is already open.
### Handling background tasks
- [func backgroundTask<D, R>(BackgroundTask<D, R>, action: (D) async -> R) -> some Scene](scene/backgroundtask(_:action:).md)
  Runs the specified action when the system provides a background task.
- [struct BackgroundTask](backgroundtask.md)
  The kinds of background tasks that your app or extension can handle.
- [struct SnapshotData](snapshotdata.md)
  The associated data of a snapshot background task.
- [struct SnapshotResponse](snapshotresponse.md)
  Your appplication’s response to a snapshot background task.
### Importing and exporting transferable items
- [func importableFromServices<T>(for: T.Type, action: ([T]) -> Bool) -> some View](view/importablefromservices(for:action:).md)
  Enables importing items from services, such as Continuity Camera on macOS.
- [func exportableToServices<T>(@autoclosure () -> [T]) -> some View](view/exportabletoservices(_:).md)
  Exports items for consumption by shortcuts, quick actions, and services.
- [func exportableToServices<T>(@autoclosure () -> [T], onEdit: ([T]) -> Bool) -> some View](view/exportabletoservices(_:onedit:).md)
  Exports read-write items for consumption by shortcuts, quick actions, and services.
### Importing and exporting using item providers
- [func importsItemProviders([UTType], onImport: ([NSItemProvider]) -> Bool) -> some View](view/importsitemproviders(_:onimport:).md)
  Enables importing item providers from services, such as Continuity Camera on macOS.
- [func exportsItemProviders([UTType], onExport: () -> [NSItemProvider]) -> some View](view/exportsitemproviders(_:onexport:).md)
  Exports a read-only item provider for consumption by shortcuts, quick actions, and services.
- [func exportsItemProviders([UTType], onExport: () -> [NSItemProvider], onEdit: ([NSItemProvider]) -> Bool) -> some View](view/exportsitemproviders(_:onexport:onedit:).md)
  Exports a read-write item provider for consumption by shortcuts, quick actions, and services.

## See Also

- [Gestures](gestures.md)
  Define interactions from taps, clicks, and swipes to fine-grained gestures.
- [Input events](input-events.md)
  Respond to input from a hardware device, like a keyboard or a Touch Bar.
- [Clipboard](clipboard.md)
  Enable people to move or duplicate items by issuing Copy and Paste commands.
- [Drag and drop](drag-and-drop.md)
  Enable people to move or duplicate items by dragging them from one location to another.
- [Focus](focus.md)
  Identify and control which visible object responds to user interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/system-events)*