# pasteDestination(for:action:validator:)

**Framework**: MusicKit  
**Kind**: method

Specifies an action that adds validated items to a view in response to the system’s Paste command.

**Availability**:
- macOS 13.0+

## Declaration

```swift
nonisolated
func pasteDestination<T>(for payloadType: T.Type = T.self, action: @escaping ([T]) -> Void, validator: @escaping ([T]) -> [T] = { $0 }) -> some View where T : Transferable
```

#### Return Value

A view that people can paste into using the system Paste command.

#### Discussion

Use this modifier to paste one or more items into a view from the Clipboard when someone issues a Paste command. People issue a Paste command by choosing Edit > Paste from the app’s menu, or by using the Command-V keyboard shortcut. The system enables the Paste command for your app when the view in focus provides a paste destination.

For example, the following code enables people to paste bird names into a list:

```swift
struct PasteDestinationExample: View {
    @State private var birds: [String] = []
    @State private var selection: Set<String> = []

    let knownBirds = ["owl", "parrot", "swift",
                      "sparrow", "robin", "bluebird"]

    var body: some View {
        List(birds, id: \.self, selection: $selection) {
            Text($0)
        }
        .pasteDestination(for: String.self) { values in
            birds.append(contentsOf: values)
        } validator: { values in
            values.filter { knownBirds.contains($0) }
        }
    }
}
```

The paste destination handles only pasted content with a type that matches the `payloadType` that you specify. The list in the above example only accepts strings.

Use the `validator` closure to restrict the pasted content to items that make sense in the context of the view. The above example allows people to paste only strings that match one of a known list of bird names because the list is meant to contain only birds. You can omit the final closure if you don’t need to perform any validation.

> **Note**: To enable people to paste using a custom action — like from a context menu item — rather than using the system Paste command, access the Clipboard directly using an [`NSPasteboard`](https://developer.apple.com/documentation/AppKit/NSPasteboard) or a [`UIPasteboard`](https://developer.apple.com/documentation/UIKit/UIPasteboard) instance.

## Parameters

- `payloadType`: The type of data that the paste destination accepts.   The type must conform to the     protocol.
- `action`: The action to perform when someone uses the system’s Paste   command to paste one or more items of the payload type. The closure   takes one parameter, which is the array of items to paste.
- `validator`: A closure that you implement to validate the data to   paste. SwiftUI calls this before it calls the   closure,   and passes in an array of items to validate. Inspect the items, and   return an array that includes only those from the input array that   you consider valid. The array that you return from this closure   becomes the input to the   closure. If you return an empty   array, SwiftUI doesn’t call the   closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/pastedestination(for:action:validator:))*