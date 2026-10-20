# SWHighlightChangeEventTrigger

**Framework**: Shared with You  
**Kind**: enum  
**Role**: Enumeration

The type of change event for the highlight

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum SWHighlightChangeEventTrigger
```

```c
enum SWHighlightChangeEventTrigger : NSInteger;
```

## Mentions

- [Adding shared content collaboration to your app](./adding-shared-content-collaboration-to-your-app.md)

## Topics

### Change actions
- [SWHighlightChangeEventTrigger.edit](./swhighlightchangeeventtrigger/edit.md)
  Signifies a highlight edit.
- [SWHighlightChangeEventTrigger.comment](./swhighlightchangeeventtrigger/comment.md)
  Signifies a highlight comment.
### Initializers
- [init?(rawValue: Int)](./swhighlightchangeeventtrigger/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing event attributes
- [var highlightURL: URL](./swhighlightchangeevent/highlighturl.md)
  The URL of the hightlight.
- [var changeEventTrigger: SWHighlightChangeEventTrigger](./swhighlightchangeevent/changeeventtrigger.md)
  The type of change event for the highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swhighlightchangeeventtrigger)*