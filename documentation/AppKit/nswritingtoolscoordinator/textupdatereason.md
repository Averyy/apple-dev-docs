# NSWritingToolsCoordinator.TextUpdateReason

**Framework**: AppKit  
**Kind**: enum

Constants that specify the reason you updated your view’s content outside of the Writing Tools workflow.

**Availability**:
- macOS 15.2+

## Declaration

```swift
enum TextUpdateReason
```

#### Overview

If you modify your view’s text storage while Writing Tools is active, report those changes to your [`NSWritingToolsCoordinator`](nswritingtoolscoordinator.md) object so it can track them correctly. Call the [`updateRange(_:with:reason:forContextWithIdentifier:)`](nswritingtoolscoordinator/updaterange(_:with:reason:forcontextwithidentifier:).md) method to report changes that occur inside one of your context objects. Call the [`updateForReflowedTextInContextWithIdentifier(_:)`](nswritingtoolscoordinator/updateforreflowedtextincontextwithidentifier(_:).md) method for changes that affect the layout of your text, such as text insertions before a context object or changes to your view’s frame rectangle.

## Topics

### Getting the reasons
- [NSWritingToolsCoordinator.TextUpdateReason.typing](nswritingtoolscoordinator/textupdatereason/typing.md)
  An operation that involved a person editing the text in your view.
- [NSWritingToolsCoordinator.TextUpdateReason.undoRedo](nswritingtoolscoordinator/textupdatereason/undoredo.md)
  An operation that changed the view’s text as part of an undo or redo command.
### Initializers
- [init?(rawValue: Int)](nswritingtoolscoordinator/textupdatereason/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func updateRange(NSRange, with: NSAttributedString, reason: NSWritingToolsCoordinator.TextUpdateReason, forContextWithIdentifier: UUID)](nswritingtoolscoordinator/updaterange(_:with:reason:forcontextwithidentifier:).md)
  Informs the coordinator about changes your app made to the text in the specified context object.
- [func updateForReflowedTextInContextWithIdentifier(UUID)](nswritingtoolscoordinator/updateforreflowedtextincontextwithidentifier(_:).md)
  Informs the coordinator that a change occurred to the view or its text that requires a layout update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/textupdatereason)*