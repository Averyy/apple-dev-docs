# automatic

**Framework**: SwiftUI  
**Kind**: property

The default text editor style, based on the text editor’s context.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency static var automatic: AutomaticTextEditorStyle { get }
```

#### Discussion

The default style represents the recommended style based on the current platform and the text editor’s context within the view hierarchy.

## See Also

- [static var plain: PlainTextEditorStyle](texteditorstyle/plain.md)
  A text editor style with no decoration.
- [static var roundedBorder: RoundedBorderTextEditorStyle](texteditorstyle/roundedborder.md)
  A text editor style with a system-defined rounded border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/texteditorstyle/automatic)*