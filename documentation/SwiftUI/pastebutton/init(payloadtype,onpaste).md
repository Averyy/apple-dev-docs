# init(payloadType:onPaste:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an instance that accepts values of the specified type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<T>(payloadType: T.Type, onPaste: @escaping ([T]) -> Void) where T : Transferable
```

## Parameters

- `payloadType`: The type that you want to paste via the `PasteButton`.
- `onPaste`: The handler to call on trigger of the button with at least one item of the specified `Transferable` type from the pasteboard.

## See Also

### Creating a paste button
- [init(supportedContentTypes: [UTType], payloadAction: ([NSItemProvider]) -> Void)](./init%28supportedcontenttypes,payloadaction%29.md)
  Creates a Paste button that accepts specific types of data from the pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pastebutton/init(payloadtype:onpaste:))*