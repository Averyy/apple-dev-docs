# init(supportedTypes:validator:payloadAction:)

**Framework**: SwiftUI  
**Kind**: init

Creates a Paste button that accepts specific types of data from the pasteboard, performing a custom validation of the data before sending it to your app.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency init<Payload>(supportedTypes: [String], validator: @escaping ([NSItemProvider]) -> Payload?, payloadAction: @escaping (Payload) -> Void)
```

#### Discussion

Set the contents of `supportedTypes` in order of your app’s preference for its supported types. The Paste button takes the most-preferred type that the pasteboard source supports and delivers this to the `validator` closure.

## Parameters

- `supportedTypes`: The exact uniform type identifiers supported   by the button. If the pasteboard doesn’t contain any of the   supported types, the button becomes disabled.
- `validator`: A handler that receives those contents of the pasteboard   that conform to  . Load and inspect these   items to determine whether to validate the button. If you load a   valid item, return it from this closure. If the pasteboard doesn’t   contain any valid items, return   to invalidate the button.
- `payloadAction`: The handler called when the user clicks the button.   This closure receives the preprocessed result of  .

## See Also

- [init(supportedTypes: [String], payloadAction: ([NSItemProvider]) -> Void)](pastebutton/init(supportedtypes:payloadaction:).md)
  Creates a Paste button that accepts specific types of data from the pasteboard.
- [init<Payload>(supportedContentTypes: [UTType], validator: ([NSItemProvider]) -> Payload?, payloadAction: (Payload) -> Void)](pastebutton/init(supportedcontenttypes:validator:payloadaction:).md)
  Creates a Paste button that accepts specific types of data from the pasteboard, performing a custom validation of the data before sending it to your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pastebutton/init(supportedtypes:validator:payloadaction:))*