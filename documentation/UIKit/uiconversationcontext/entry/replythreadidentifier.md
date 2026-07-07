# replyThreadIdentifier

**Framework**: UIKit  
**Kind**: property

An optional string that identifies another message in a conversation, when this entry is a reply to that message.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

## Declaration

```swift
var replyThreadIdentifier: String? { get set }
```

#### Discussion

When an entry is a reply to another conversation entry, this contains the identifier of the conversation entry that the person replied to.

## See Also

- [var entryIdentifier: String](uiconversationcontext/entry/entryidentifier.md)
  A string that uniquely identifies this specific entry in the conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiconversationcontext/entry/replythreadidentifier)*