# NSWritingToolsCoordinator.TextDecoration

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Use the `NSWritingToolsCoordinator.TextDecoration` constants to determine the type of decoration to be applied to a preview for grammar animation. The grammar animation needs previews of the text of the issue in two forms, without and with the grammar indication underline applied. If you use grammar animation, you must implement the delegate method [`writingToolsCoordinator(_:requestsPreviewFor:of:in:textDecoration:completion:)`](./delegate-swift.protocol/writingtoolscoordinator%28_,requestspreviewfor,of,in,textdecoration,completion%29.md) to provide both forms of previews, based on the specified decoration.

**Availability**:
- macOS 27.0+

## Declaration

```swift
enum TextDecoration
```

```c
enum NSWritingToolsCoordinatorTextDecoration : NSInteger;
```

## Topics

### Enumeration Cases
- [NSWritingToolsCoordinator.TextDecoration.grammarUnderline](./textdecoration/grammarunderline.md)
  Requests a preview of the text with the grammar indication underline.
- [NSWritingToolsCoordinator.TextDecoration.none](./textdecoration/none.md)
  Requests a preview of the text without any additional decoration.
### Initializers
- [init?(rawValue: Int)](./textdecoration/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/textdecoration)*