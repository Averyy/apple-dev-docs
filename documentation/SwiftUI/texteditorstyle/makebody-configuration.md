# makeBody(configuration:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates a view that represents the body of a text editor.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@ViewBuilder
@MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

#### Discussion

The system calls this method for each [`TextEditor`](texteditor.md) instance in a view hierarchy where this style is the current text editor style.

## Parameters

- `configuration`: The properties of the text editor.

## See Also

- [TextEditorStyle.Configuration](texteditorstyle/configuration.md)
  The properties of a text editor.
- [associatedtype Body : View](texteditorstyle/body.md)
  A view that represents the body of a text editor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/texteditorstyle/makebody(configuration:))*