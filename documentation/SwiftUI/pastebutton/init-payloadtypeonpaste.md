# init(payloadType:onPaste:)

**Framework**: SwiftUI  
**Kind**: init

Creates an instance that accepts values of the specified type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency init<T>(payloadType: T.Type, onPaste: @escaping ([T]) -> Void) where T : Transferable
```

## Parameters

- `onPaste`: The handler to call on trigger of the button with at least   one item of the specified   type from the pasteboard.

## See Also

- [init(supportedContentTypes: [UTType], payloadAction: ([NSItemProvider]) -> Void)](pastebutton/init(supportedcontenttypes:payloadaction:).md)
  Creates a Paste button that accepts specific types of data from the pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pastebutton/init(payloadtype:onpaste:))*