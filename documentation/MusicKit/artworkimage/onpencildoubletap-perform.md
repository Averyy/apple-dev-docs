# onPencilDoubleTap(perform:)

**Framework**: MusicKit  
**Kind**: method

Adds an action to perform after the user double-taps their Apple Pencil.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- macOS 14.5+

## Declaration

```swift
nonisolated
func onPencilDoubleTap(perform action: @escaping (PencilDoubleTapGestureValue) -> Void) -> some View
```

#### Return Value

A view that performs `action` after the user double-taps their Apple Pencil.

#### Discussion

You should respect people’s setting for the double-tap gesture by reading the `EnvironmentValues/preferredPencilDoubleTapAction` environment value, if the setting makes sense in your app. If it doesn’t, consider giving people a way to specify custom behavior in your app instead.

In the example below, double-tapping an Apple Pencil will…

- do nothing if this is what the user selected in the Settings app,
- switch the tool to ”Lasso” if this is the action they have configured in the app,
- switch the tool to ”Eraser” if they haven’t configured a custom action in the app and this is what they selected in the Settings app,
- switch the tool to the last used one otherwise.

```swift
enum MyDrawingTool: Equatable {
    case brush
    case lasso
    case eraser
    ...
}

enum MyPencilAction: String {
    case switchLasso
    ...
}

@State private var currentTool = MyDrawingTool.brush
@State private var lastTool: MyDrawingTool?

@Environment(\.preferredPencilDoubleTapAction) private var globalAction
@AppStorage("customPencilDoubleTapAction") private var customAction: MyPencilAction?

var body: some View {
    MyDrawingCanvas()
        .onPencilDoubleTap { _ in
            guard globalAction != .ignore else {
                // Respect the user’s preference to ignore the double-tap gesture.
                return
            }
            if let customAction {
                // If a custom action is configured, respect it.
                if customAction == .switchLasso, currentTool != .lasso {
                     (currentTool, lastTool) = (.lasso, currentTool)
                }
            } else if globalAction == .switchEraser, currentTool != .eraser {
                // Switch to eraser if the user prefers it otherwise.
                (currentTool, lastTool) = (.eraser, currentTool)
            } else if let lastTool {
                // Switch to the last used tool by default.
                (currentTool, lastTool) = (lastTool, currentTool)
            }
        }
}
```

For more information about Apple Pencil double-tap gestures, see [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble#Double-tap).

> **Note**: If multiple views with the `onPencilDoubleTap` view modifier are visible, all their action closures will be performed after the user double-taps their Apple Pencil.

## Parameters

- `action`: The action to perform after the user double-taps their   Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/onpencildoubletap(perform:))*