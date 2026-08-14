# NSWritingToolsCoordinator.TextDecoration

**Framework**: AppKit  
**Kind**: enum

Use the `NSWritingToolsCoordinator.TextDecoration` constants to determine the type of decoration to be applied to a preview for grammar animation. The grammar animation needs previews of the text of the issue in two forms, without and with the grammar indication underline applied. If you use grammar animation, you must implement the delegate method [`writingToolsCoordinator(_:requestsPreviewFor:of:in:textDecoration:completion:)`](nswritingtoolscoordinator/delegate-swift.protocol/writingtoolscoordinator(_:requestspreviewfor:of:in:textdecoration:completion:).md) to provide both forms of previews, based on the specified decoration.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
enum TextDecoration
```

## Topics

### Enumeration Cases
- [NSWritingToolsCoordinator.TextDecoration.grammarUnderline](nswritingtoolscoordinator/textdecoration/grammarunderline.md)
  Requests a preview of the text with the grammar indication underline.
- [NSWritingToolsCoordinator.TextDecoration.none](nswritingtoolscoordinator/textdecoration/none.md)
  Requests a preview of the text without any additional decoration.
### Initializers
- [init?(rawValue: Int)](nswritingtoolscoordinator/textdecoration/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/textdecoration)*