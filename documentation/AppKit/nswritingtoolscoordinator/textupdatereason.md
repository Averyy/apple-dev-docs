# NSWritingToolsCoordinator.TextUpdateReason

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the reason you updated your view’s content outside of the Writing Tools workflow.

**Availability**:
- macOS 15.2+

## Declaration

```swift
enum TextUpdateReason
```

```c
enum NSWritingToolsCoordinatorTextUpdateReason : NSInteger;
```

## Overview

If you modify your view’s text storage while Writing Tools is active, report those changes to your [`NSWritingToolsCoordinator`](../nswritingtoolscoordinator.md) object so it can track them correctly. Call the [`updateRange(_:with:reason:forContextWithIdentifier:)`](./updaterange%28_,with,reason,forcontextwithidentifier%29.md) method to report changes that occur inside one of your context objects. Call the [`updateForReflowedTextInContextWithIdentifier(_:)`](./updateforreflowedtextincontextwithidentifier%28_%29.md) method for changes that affect the layout of your text, such as text insertions before a context object or changes to your view’s frame rectangle.

## Topics

### Getting the reasons
- [NSWritingToolsCoordinator.TextUpdateReason.typing](./textupdatereason/typing.md)
  An operation that involved a person editing the text in your view.
- [NSWritingToolsCoordinator.TextUpdateReason.undoRedo](./textupdatereason/undoredo.md)
  An operation that changed the view’s text as part of an undo or redo command.
### Initializers
- [init?(rawValue: Int)](./textupdatereason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Reporting changes to Writing Tools
- [func updateRange(NSRange, with: NSAttributedString, reason: NSWritingToolsCoordinator.TextUpdateReason, forContextWithIdentifier: UUID)](./updaterange%28_,with,reason,forcontextwithidentifier%29.md)
  Informs the coordinator about changes your app made to the text in the specified context object.
- [func updateForReflowedTextInContextWithIdentifier(UUID)](./updateforreflowedtextincontextwithidentifier%28_%29.md)
  Informs the coordinator that a change occurred to the view or its text that requires a layout update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/textupdatereason)*