# init(supportedTypes:payloadAction:)

**Framework**: SwiftUI  
**Kind**: init

Creates a Paste button that accepts specific types of data from the pasteboard.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency init(supportedTypes: [String], payloadAction: @escaping ([NSItemProvider]) -> Void)
```

#### Discussion

Set the contents of `supportedTypes` in order of your app’s preference for its supported types. The Paste button takes the most-preferred type that the pasteboard source supports and delivers this to the `payloadAction` closure.

## Parameters

- `supportedTypes`: The exact uniform type identifiers supported   by the button. If the pasteboard doesn’t contain any of the   supported types, the button becomes disabled.
- `payloadAction`: The handler to call when the user clicks the Paste   button, and the pasteboard has items that conform to   . This closure receives an array of   item providers that you use to inspect and load the pasteboard data.

## See Also

- [init<Payload>(supportedTypes: [String], validator: ([NSItemProvider]) -> Payload?, payloadAction: (Payload) -> Void)](pastebutton/init(supportedtypes:validator:payloadaction:).md)
  Creates a Paste button that accepts specific types of data from the pasteboard, performing a custom validation of the data before sending it to your app.
- [init<Payload>(supportedContentTypes: [UTType], validator: ([NSItemProvider]) -> Payload?, payloadAction: (Payload) -> Void)](pastebutton/init(supportedcontenttypes:validator:payloadaction:).md)
  Creates a Paste button that accepts specific types of data from the pasteboard, performing a custom validation of the data before sending it to your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pastebutton/init(supportedtypes:payloadaction:))*