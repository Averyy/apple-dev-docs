# PasteButton

**Framework**: SwiftUI  
**Kind**: struct

A system button that reads items from the pasteboard and delivers it to a closure.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency struct PasteButton
```

#### Overview

Use a paste button when you want to provide a button for pasting items from the system pasteboard into your app. The system provides a button appearance and label appropriate to the current environment. However, you can use view modifiers like [`buttonBorderShape(_:)`](view/buttonbordershape(_:).md), [`labelStyle(_:)`](view/labelstyle(_:).md), and [`tint(_:)`](view/tint(_:).md) to customize the button in some contexts.

You declare what type of items your app will accept; use a type that conforms to the [`Transferable`](https://developer.apple.com/documentation/CoreTransferable/Transferable) protocol. When the user taps or clicks the button, your closure receives the pasteboard items in the specified type.

In the following example, a paste button declares that it accepts a string. When the user taps or clicks the button, the sample’s closure receives an array of strings and sets the first as the value of `pastedText`, which updates a nearby [`Text`](text.md) view.

```swift
@State private var pastedText: String = ""

var body: some View {
    HStack {
        PasteButton(payloadType: String.self) { strings in
            pastedText = strings[0]
        }
        Divider()
        Text(pastedText)
        Spacer()
    }
}
```

![macOS window titled PasteButton Demo showing (from left to right) a button](https://docs-assets.developer.apple.com/published/f7c7294618325966191dfa4e305ff625/SwiftUI-PasteButton-pastedText%402x.png)

A paste button automatically validates and invalidates based on changes to the pasteboard on iOS, but not on macOS.

## Topics

### Creating a paste button
- [init(supportedContentTypes: [UTType], payloadAction: ([NSItemProvider]) -> Void)](pastebutton/init(supportedcontenttypes:payloadaction:).md)
  Creates a Paste button that accepts specific types of data from the pasteboard.
- [init<T>(payloadType: T.Type, onPaste: ([T]) -> Void)](pastebutton/init(payloadtype:onpaste:).md)
  Creates an instance that accepts values of the specified type.
### Deprecated initializers
- [init(supportedTypes: [String], payloadAction: ([NSItemProvider]) -> Void)](pastebutton/init(supportedtypes:payloadaction:).md)
  Creates a Paste button that accepts specific types of data from the pasteboard.
- [init<Payload>(supportedTypes: [String], validator: ([NSItemProvider]) -> Payload?, payloadAction: (Payload) -> Void)](pastebutton/init(supportedtypes:validator:payloadaction:).md)
  Creates a Paste button that accepts specific types of data from the pasteboard, performing a custom validation of the data before sending it to your app.
- [init<Payload>(supportedContentTypes: [UTType], validator: ([NSItemProvider]) -> Payload?, payloadAction: (Payload) -> Void)](pastebutton/init(supportedcontenttypes:validator:payloadaction:).md)
  Creates a Paste button that accepts specific types of data from the pasteboard, performing a custom validation of the data before sending it to your app.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [struct EditButton](editbutton.md)
  A button that toggles the edit mode environment value.
- [struct RenameButton](renamebutton.md)
  A button that triggers a standard rename action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pastebutton)*