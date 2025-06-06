# onPencilSqueeze(perform:)

**Framework**: Managedappdistribution  
**Kind**: method

Adds an action to perform when the user squeezes their Apple Pencil.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- macOS 14.5+

## Declaration

```swift
nonisolated
func onPencilSqueeze(perform action: @escaping (PencilSqueezeGesturePhase) -> Void) -> some View
```

#### Return Value

A view that performs `action` when the user squeezes their Apple Pencil.

#### Discussion

You should respect people’s setting for the squeeze gesture by reading the `EnvironmentValues/preferredPencilSqueezeAction` environment value, if the setting makes sense in your app. If it doesn’t, consider giving people a way to specify custom behavior in your app instead.

In the example below, completing an Apple Pencil squeeze gesture will…

- do nothing if this is what the user selected in the Settings app,
- switch the tool to ”Lasso” if this is the action they have configured in the app,
- spill the ink if this is the action they have configured in the app,
- present a custom contextual palette if they haven’t configured a custom action in the app and this is what they selected in the Settings app.

```None
enum MyPencilAction: String {
    case spillInk
    ...
}

@Environment(\.preferredPencilSqueezeAction) private var preferredAction
@AppStorage("customPencilSqueezeAction") private var customAction: MyPencilAction?

@State private var contextualPaletteAnchor: PopoverAttachmentAnchor?
@State private var contextualPalettePresented = false

var body: some View {
    MyDrawingCanvas()
        .onPencilSqueeze { phase in
            guard preferredAction != .ignore else {
                // Skip if this is what the user prefers.
                return
            }
            if let customAction {
                // If a custom action is configured, respect it.
                if customAction == .spillInk {
                    switch phase {
                        // Spill the ink while the user is squeezing their Apple Pencil.
                    }
                }
            } else if preferredAction == .showContextualPalette, case let .ended(value) = phase {
                // Present a custom contextual palette if the user prefers it.
                contextualPaletteAnchor = value.hoverPose?.anchor.map { .point($0) }
                contextualPalettePresented = true
            }
        }
        .popover(
            isPresented: $contextualPalettePresented,
            attachmentAnchor: contextualPaletteAnchor ?? .point(.center)
        ) {
            MyContextualPalette()
        }
```

> **Note**: If multiple views with the `onPencilSqueeze` view modifier are visible, all their action closures will be performed when the user squeezes their Apple Pencil.

## Parameters

- `action`: The action to perform when the user squeezes their   Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedcontentview/onpencilsqueeze(perform:))*