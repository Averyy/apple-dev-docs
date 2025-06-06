# onPasteCommand(of:validator:perform:)

**Framework**: RealityKit  
**Kind**: method

Adds an action to perform in response to the system’s Paste command with items that you validate.

**Availability**:
- macOS 10.15+

## Declaration

```swift
nonisolated
func onPasteCommand<Payload>(of supportedTypes: [String], validator: @escaping ([NSItemProvider]) -> Payload?, perform payloadAction: @escaping (Payload) -> Void) -> some View
```

#### Return Value

A view that triggers `action` when the system Paste command is invoked, validating the Paste command with `validator`.

#### Discussion

Pass an array of uniform type identifiers to the `supportedTypes` parameter. Place the higher priority types closer to the beginning of the array. The Clipboard items that the `validator` closure receives have the most preferred type out of all the types the source supports.

For example, if your app can handle plain text and rich text, but you prefer rich text, place the rich text type first in the array. If rich text is available when the paste action occurs, the `validator` closure passes that rich text along.

## Parameters

- `supportedTypes`: The uniform type identifiers that describe the   types of content this view can accept through a paste action.   If the Clipboard doesn’t contain any of the supported types, the   Paste command doesn’t trigger.
- `validator`: A handler that validates the command. This handler   receives items from the Clipboard with the types you specify in the    parameter. Use this handler to decide whether   the items are valid and preprocess them for the   closure.   If you return   instead, the Paste command doesn’t trigger.
- `payloadAction`: The action to perform when the Paste command triggers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/onpastecommand(of:validator:perform:)-6w6e)*